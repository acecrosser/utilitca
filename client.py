import sys
import os
from datetime import datetime
from PySide2 import QtWidgets
from functions import complex_settings, fiscal_and_reg, request_for_work
from functions import make_mail, data_type, data_path, fiscal_kkt, request, request_online
from interFaceUtil import Ui_mainWindow


class ReportGroupApp(QtWidgets.QMainWindow, Ui_mainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.constant_data = dict()
        self.list_type = dict()

        self.comboBox.setItemData(0, 'fiscal')
        self.comboBox.setItemData(1, 'complex')
        self.comboBox.setItemData(2, 'market')
        self.comboBox.setItemData(3, 'perereg_off_fn')
        self.comboBox.setItemData(4, 'perereg_on_fn')
        self.comboBox.setItemData(5, 'ssu')
        self.comboBox.setItemData(6, 'update')
        self.comboBox.setItemData(7, 'blank')

        self.printReestr.clicked.connect(self.make_registry_report)
        self.printRequest.clicked.connect(self.make_request_report)
        self.makeEmail.clicked.connect(self.send_mail)

    def make_data(self):
        d_name_company = self.name_company.text()
        d_address_work = self.address_work.text()
        d_inn_company = self.inn_company.text()
        d_kpp_company = self.kpp_company.text()
        d_number_bill = self.number_bill.text()
        d_model_kkt = self.model_kkt.text()
        d_serial_kkt = self.serial_kkt.text()
        d_serial_fn = self.serial_fn.text()
        spec_name = self.spec_name.text()

        combobox_item = self.comboBox.currentData()
        service_text = self.comboBox.currentText()

        registry_data = {
            'C1': datetime.now().strftime('%d.%m.%Y'),
            'C2': d_name_company,
            'C3': d_address_work,
            'C5': d_inn_company,
            'C6': d_kpp_company,
            'C7': d_number_bill,
            'H2': d_model_kkt,
            'H3': d_serial_kkt,
            'H5': d_serial_fn,
        }

        request_data = {
             'B1': datetime.now().strftime('%d.%m.%Y'),
             'E1': f'{d_inn_company}-{d_kpp_company}',
             'E2': d_name_company,
             'E4': d_number_bill,
             'E5': service_text,
             'E13': d_model_kkt,
             'E14': d_serial_kkt,
             'E15': d_serial_fn,
        }

        return {
            'data': registry_data,
            'request_data': request_data,
            'item': combobox_item,
            'name': spec_name,
        }

    def make_registry_report(self):

        combobox_item = self.make_data()['item']
        spec_name = self.make_data()['name']
        registry_data = self.make_data()['data']

        if combobox_item == 'fiscal':
            fiscal_and_reg(spec_name, **registry_data)
            os.system(f'start excel.exe "{data_path}{fiscal_kkt}"')
        else:
            complex_settings(spec_name, data_type[combobox_item][0], *data_type[combobox_item], **registry_data)
            os.system(f'start excel.exe "{data_path}{data_type[combobox_item][0]}"')

    def make_request_report(self):

        combobox_item = self.make_data()['item']
        request_data = self.make_data()['request_data']

        d_model_kkt = request_data['E13']
        d_serial_kkt = request_data['E14']

        if combobox_item == 'update':
            request_data.pop('E13')
            request_data.pop('E14')
            request_data.pop('E15')
            request_data.pop('E5')
            request_data.update({'E9': d_model_kkt})
            request_data.update({'E10': d_serial_kkt})
            request_for_work(request_online, **request_data)
            os.system(f'start excel.exe "{data_path}{request_online}"')
        else:
            request_for_work(request, **request_data)
            os.system(f'start excel.exe "{data_path}{request}"')

    def send_mail(self):

        combobox_item = self.make_data()['item']
        spec_name = self.make_data()['name']
        registry_data = self.make_data()['data']
        request_data = self.make_data()['request_data']

        d_model_kkt = request_data['E13']
        d_serial_kkt = request_data['E14']

        if self.checkBox.isChecked():
            if combobox_item == 'update':
                request_data.pop('E13')
                request_data.pop('E14')
                request_data.pop('E15')
                request_data.update({'E9': d_model_kkt})
                request_data.update({'E10': d_serial_kkt})
                request_for_work(request_online, **request_data)
                make_mail(f'{request_online}')
            else:
                request_for_work(request, **request_data)
                make_mail(f'{request}')
        else:
            if combobox_item == 'fiscal':
                fiscal_and_reg(spec_name, **registry_data)
                make_mail(f'{fiscal_kkt}')
            else:
                complex_settings(spec_name, data_type[combobox_item][0], *data_type[combobox_item], **registry_data)
                make_mail(data_type[combobox_item][0])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mrg = ReportGroupApp()
    mrg.show()
    sys.exit(app.exec_())
