import smartcard
from smartcard.System import readers
from smartcard.util import toHexString

# Tìm các đầu đọc thẻ được kết nối
r = readers()
if len(r) == 0:
    print("Không tìm thấy đầu đọc thẻ nào")
else:
    print("Đầu đọc thẻ tìm thấy: ", r)

# Chọn đầu đọc thẻ đầu tiên
reader = r[0]
connection = reader.createConnection()
connection.connect()

# Gửi lệnh SELECT để chọn ứng dụng trên thẻ
SELECT = [0x00, 0xA4, 0x04, 0x00, 0x07, 0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10]
response, sw1, sw2 = connection.transmit(SELECT)
if sw1 == 0x90 and sw2 == 0x00:
    print("Ứng dụng đã được chọn thành công")
else:
    print("Lỗi khi chọn ứng dụng, mã trạng thái: %02X %02X" % (sw1, sw2))

# Gửi lệnh GET PROCESSING OPTIONS để lấy thông tin thẻ
GET_PROCESSING_OPTIONS = [0x80, 0xA8, 0x00, 0x00, 0x02, 0x83, 0x00, 0x00]
response, sw1, sw2 = connection.transmit(GET_PROCESSING_OPTIONS)
if sw1 == 0x90 and sw2 == 0x00:
    print("Thông tin thẻ:", toHexString(response))
else:
    print("Lỗi khi lấy thông tin thẻ, mã trạng thái: %02X %02X" % (sw1, sw2))
