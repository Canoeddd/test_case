
from py_page.temu_p_net import TemuNet
from page_locator.public import des1, des2, link_net, code_net
from log.get_log import log_error

class TestNet():

    def test_coupon_des(self):

        # log_file_path = r'..\log\站群.txt'
        store_detail = TemuNet()
        c1 = store_detail.first_des()
        c2 = store_detail.sec_des()
        print(c1)
        print(c2)

        try:
            print("*-*" * 28,"【判断coupon的描述】","*-*" * 28)
            assert c1 == des1 and c2 == des2, f"WA0298-net 前两张coupon的描述内容错误"    #  coupon描述断言

        except AssertionError as AE:
            print(AE)
            # error_log = str(AE)
            # log_error(log_file_path, error_log)




    def test_get_deal_link(self):

        # log_file_path = r'..\log\站群.txt'
        store_detail = TemuNet()

        try:
            get_deal_net = store_detail.link_ele()
            print(get_deal_net)
            assert get_deal_net == link_net, f"WA0298-net get deal的affi-Link链接错误"   #  get deal的affi-Link断言

        except AssertionError as AE:
            print(AE)
            # error_log = str(AE)
            # log_error(log_file_path, error_log)



    def test_first_coupon(self):

        # log_file_path = r'..\log\站群.txt'
        store_detail = TemuNet()

        try:

            affi_code1 = store_detail.first_code()
            print(affi_code1)
            assert affi_code1 == code_net, f"WA0298-net的第一个affi-Code错误"

            store_detail.copy_code()
            affi_code1_link = store_detail.code_link()
            assert affi_code1_link == link_net, f"WA0298-net的第一个affi-link错误"

        except AssertionError as AE:
            print(AE)
            # error_log = str(AE)
            # log_error(log_file_path, error_log)



    def test_sec_coupon(self):

        # log_file_path = r'..\log\站群.txt'
        store_detail = TemuNet()

        try:
            affi_code2 = store_detail.sec_code()
            print(affi_code2)
            assert affi_code2 == code_net, f"WA0298-net的第二个affi-Code错误"

            store_detail.copy_code()
            affi_code2_link = store_detail.code_link()
            assert affi_code2_link == link_net, f"WA0298-net的第二个affi-link错误"

        except AssertionError as AE:
            print(AE)
            # error_log = str(AE)
            # log_error(log_file_path, error_log)

    # except AssertionError as AE:
    #     print(str(AE))


#
# if __name__ == '__main__':
#     pytest.main(['-v', 'test_ofs.py'])