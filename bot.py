import time
import sys
import re
import threading


from PyQt5 import QtWidgets
import requests
from lxml import html
from bs4 import BeautifulSoup


from racer_ui import Ui_MainWindow
from utils import form_encode, fix_wh, OpenBox


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def UploadId():
    id_from_field = ui.lineEdit.text().split(',')
    id_list = []
    for i in id_from_field:
        id_list.append(i.replace(' ', ''))

    return id_list


def check_auth():
    link = ui.auth_link.text()
    if link != '':
        auth_link = requests.get(link)
        if 'Гонки' in auth_link.text:
            ui.auth_text_status.setText("<font color='green'>Ссылка работает</font>")
            return True
        else:
            ui.auth_text_status.setText("<font color='red'>Ошибка авторизации</font>")
            return False
    else:
        pass

def Auth(auth_link):
    global search_taxi_link
    main_page = requests.get(auth_link)
    if 'Гонки' in main_page.text:
        # опередяем через что юзер играет
        if "stracing.mobi/race_dev/public/oauth.php" in auth_link:
            half_link = "http://stracing.mobi/race_dev/public/oauth.php"

        elif "stracing.mobi/race_dev/public/vk.php" in auth_link:
            half_link = "http://stracing.mobi/race_dev/public/vk.php"

        else:
            half_link = "http://stracing.mobi/race_dev/mobile/index.php"
            half_link = half_link.replace('https', 'http')

        if 'Сменить интерфейс' in main_page.text and 'iframe-topline-table' in main_page.text:
            web_page = html.fromstring(main_page.content)
            for i in web_page.xpath('//a/@href'):
                if '?sr_method=changeInterface' in i:
                    change_i_link = i
            #  меняем интерфейс и дальше ищем в нем нужные ссылки
            change_interface = requests.get(half_link + change_i_link)
            #  парсим ссылку конкуренты
            web_page = html.fromstring(change_interface.content)
            for i in web_page.xpath('//a/@href'):
                if '?sr_method=taxi' in i:
                    c_list = i
        else:
            web_page = html.fromstring(main_page.content)
            for i in web_page.xpath('//a/@href'):
                if '?sr_method=taxi' in i:
                    c_list = i
        #  Переходим в конкуренты
        try:
            conc = requests.get(half_link + c_list)
            taxi_page = html.fromstring(conc.content)
            # получаем ссылку на поиск
            for s in taxi_page.xpath('//a/@href'):
                if '?sr_method=searchClan' in s:
                    search_taxi_link = s
                    search_taxi_page = (half_link + search_taxi_link)
            #  переходим в поиск
            search_page = requests.get(half_link + search_taxi_link)

            if 'Поиск по такси' in search_page.text:  # авторизованы
                auth_done = True
        except:
            pass

        return search_taxi_page, half_link


def Box(stop):
    #  Коробки
    id_range_min = ui.spinBox.value()
    id_range_max = ui.spinBox_2.value()
    lnk = ui.auth_link.text()
    link, half_link = Auth(lnk)
    total_box = 0
    taxi_id_tuple = [s for s in range(id_range_min, id_range_max)]
    for i in taxi_id_tuple:
        if stop():
            break
        src = requests.get(link + "&sstr=&sstr_id={}".format(i))
        parse_id_link = html.fromstring(src.content)
        for k in parse_id_link.xpath('//a/@href'):
            if '?sr_method=enterClan&' in k:  # если нашли по ид
                #  переходим в такси если нашли
                nav_to_taxi = requests.get(half_link + k)
                #  ищем ссылку статистика и жмем на неё
                wp = html.fromstring(nav_to_taxi.content)
                for z in wp.xpath('//a/@href'):
                    if 'sr_method=showClanStatistic' in z:
                        clan_statistics_link = half_link + z
                        #  заходим в статистику
                        nav_to_stat = requests.get(clan_statistics_link)
                        soup = BeautifulSoup(nav_to_stat.text, 'html.parser')
                        fl = soup.find('td', align='left').getText()
                        #  считаем сколько ссылок на гаражи и переходим в гаражи
                        gp = html.fromstring(nav_to_stat.content)
                        for q in gp.xpath('//a/@href'):
                            if 'sr_method=getEnemyGarage' in q:
                                taxist_garage_link = []
                                taxist_garage_link.append(half_link + q)
                                for j in taxist_garage_link:
                                    nav_to_garage = requests.get(j)
                                    if 'b-box' in nav_to_garage.text:
                                        current_box_value = ui.box_count.text()
                                        current_box_value = int(current_box_value)
                                        current_box_value += 1
                                        ui.box_count.setText(str(current_box_value))
                                        gs = html.fromstring(nav_to_garage.content)
                                        for q in gs.xpath('//a/@href'):
                                            if '?sr_method=tryOpenPresentBox' in q:
                                                open_box = half_link + q
                                                total_box += 1
                                            #  жмем сундук и смотрим платный ли
                                                open = requests.get(open_box)  # открываем первый раз
                                                if 'Сундук закрыт' in open.text:  # если закрыт
                                                    sp = BeautifulSoup(open.text, 'html.parser')
                                                    open_box_btn = sp.find('form')
                                                    open_box_btn = str(open_box_btn)
                                                    try_to_open = OpenBox(open_box_btn, half_link)
                                                    requests.get(try_to_open)
                                    else:
                                        continue


def StartRacing(stop):
    link = ui.auth_link.text()
    search_taxi_page,half_link = Auth(link)
    id_list = UploadId()
    taxi_id_tuple = id_list
    taxi_url_list = []
    #  теперь добавляем к урлу нужный ids
    for i in taxi_id_tuple:
        if stop():
            break
        src = requests.get(search_taxi_page + "&sstr=&sstr_id={}".format(i))
        parse_id_link = html.fromstring(src.content)
        for k in parse_id_link.xpath('//a/@href'):
            if '?sr_method=enterClan&' in k: #  если нашли по ид
                #  сохраняем ссылки на переходы в такси
                taxi_url_list.append(half_link + k)
    for t in taxi_url_list:
        if stop():
            break
        total_race = 0
        navigate_to_taxi = requests.get(t)
        enemy_count = re.findall('clanRace', str(navigate_to_taxi.text))
        total_win = 0
        total_lose = 0
        #  нужно проверять кол-во гоншиков через статистику клана
        for i in range(len(enemy_count * 3)):
            if stop():
                break
            navigate_to_taxi = requests.get(t)
            soup = BeautifulSoup(navigate_to_taxi.text, 'html.parser')
            form = soup.find('form')
            fl = soup.find('span', id='FUELCNT').getText()
            form = str(form)
            race_link = form_encode(form, half_link)
            after_race = requests.get(race_link)
            if "Победа" in after_race.text:
                total_win += 1
                current_win_race_label_value = ui.win_count.text()
                current_win_race_label_value = int(current_win_race_label_value)
                current_win_race_label_value += 1
                ui.win_count.setText(str(current_win_race_label_value))
            elif "Поражение" in after_race.text:
                total_lose += 1
                current_win_race_label_value = ui.loose_count.text()
                current_win_race_label_value = int(current_win_race_label_value)
                current_win_race_label_value += 1
                ui.loose_count.setText(str(current_win_race_label_value))
            total_race += 1
            #  починка колеса TODO: эта функция пока не работает, да и не будет, ибо мне похуй на неё.
            if 'У тебя проколото колесо' in after_race.text:  # есть проколотое колесо, фиксим
                sp = BeautifulSoup(after_race.text, 'html.parser')
                fix_wheel = sp.find('form')
                fix_wheel = str(fix_wheel)
                fix_wheel_link = fix_wh(fix_wheel[1], half_link)
                requests.get(fix_wheel_link)
            if int(fl) < 10:
                time.sleep(2160)


def stop():
    return True


def StartWork(stop=False):
    global stop_threads
    global stop_race
    if check_auth():
        if ui.box_radio.isChecked():
            if stop == True:
                stop_threads = True
                ui.start_btn.setEnabled(True)
            else:
                stop_threads = False
                taxi_thread = threading.Thread(target=Box,name='BoxThread',args=(lambda : stop_threads,))
                taxi_thread.daemon = True
                taxi_thread.start()
                ui.start_btn.setEnabled(False)
        elif ui.racing_radio.isChecked():
            if stop == True:
                stop_race = True
                ui.start_btn.setEnabled(True)
            else:
                stop_race = False
                racing_thread = threading.Thread(target=StartRacing,name='RacingThread',args=(lambda : stop_race,))
                racing_thread.daemon = True
                racing_thread.start()
                ui.start_btn.setEnabled(False)


ui.check_link.clicked.connect(check_auth)
ui.start_btn.clicked.connect(StartWork)
ui.stop_btn.clicked.connect(lambda:StartWork(stop=True))
if __name__ == "main":
    pass
sys.exit(app.exec_())
