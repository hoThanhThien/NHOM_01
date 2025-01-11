# NHOM_01
ID Đề Tài 01
#      DiamondShopSystem
Phần mềm quản lý cửa hàng kim cương
NHÓM 01
ID Đề Tài 01
TÀI LIỆU ĐẶC TẢ YÊU CẦU PHẦN MỀM
DiamondShopSystem
Phần mềm quản lý cửa hàng kim cương
Ký hiệu phần mềm : DSS 
Phiên Bản : DSS 1.0
Tác giả: Nhóm 01
Ngày tạo:28/11/2024
Thuộc Đơn vị/ Tổ chức: Group One 
Mục Lục
Lịch Sử Tài Liệu	
Danh sách các hình	
Thuật ngữ	
I.  Giới Thiệu Chung	
1.Mục đích	
2.Phạm vi sản phẩm	
II. Mô tả Tổng Quát	
1. Chức năng	
2. Phân loại Người dùng	
3. Môi trường thiết kế & xây dựng	
III.  Yêu Cầu Tương tác Ngoài	
1.Giao diện người dùng	
2.Yêu cầu tương tác với phần cứng	
3.Yêu Cầu tương tác với phần mềm	
IV. Kiến Trúc hệ thống	
IV.1 Kiến trúc Tổng Thể của hệ Thống	
IV.2 Chi tiết các thành phần	
IV.2.1 Front End	
IV.2.2 Back End	
V. Yêu cầu phi chức năng	
VI. Các yêu cầu khác	
VII. Phục Lục	

Lịch Sử Tài Liệu

Tên Mục thay đổi
Thời gian
Lý Do
Hành động
Người thay đổi
Các phiên bản
Tài liệu Đặc tả
28/11/2024
Tạo tài liệu
khởi tạo file
Thành Thiện
DSS 1.0
Bổ sung hình ảnh
05/01/2025
hình 11
chèn ảnh
Thành Thiện
DSS 1.5


Danh sách các hình
	Hình 1: Các actor của hệ thống
	Hình 2: Component diagram
	Hình 3: Deployment diagram
	Hình 4: class diagram
	Hình 5: Hình use-case của Guest
	Hình 6: Hình use-case của Customer
	Hình 7: Admin use-case diagram
	Hình 8: Quản lý nhân viên 
	Hình 9: Activity diagram thêm nhân viên
	Hình 10:Sequence diag. thêm nhân viên

	
Thuật ngữ
	
Thuật ngữ
Viết Tắt
Nội dung
Chú Thích
Software Requirement Specification
SRS
Bản đặc tả phần mềm


Diamond Shop System
DSS
Phần Mềm quản lý kim cương


Guest


Người ghé thăm trang web này
Chưa có đăng nhập hoặc chưa có tài khoản.
Customer


Khách hàng
Khách hàng, có thể thực hiện việc mua hàng.
Product


Sản phẩm
Các sản phẩm trang sức của cửa hàng
Employee (Nhân viên) trong đó gồm:
Manager
Sales Staff
Delivery Staff






Nhân viên quản lý
Nhân viên bán hàng
Nhân viên giao hàng




1.Có quyền quản lý cửa hàng nhưng không cao hơn admin
2.Phụ trách bán hàng
3.Phụ trách giao hàng



Admin


Quản trị hệ thống
Quyền tối cao
Shopping cart


Giỏ hàng
Chứa các mục hàng
Category


Danh mục sản phẩm


Order


Hóa đơn


Account


Tài khoản
Bao gồm các thông tin cá nhân
User


Là người có tài khoản
Bao gồm các thông tin cơ bản











I.  Giới Thiệu Chung
1.Mục đích
DiamondShopSystem là một nền tảng thương mại điện tử, cung cấp cho khách hàng khả năng đăng ký tài khoản, tra cứu thông tin sản phẩm và thực hiện giao dịch mua sắm trực tuyến một cách thuận tiện.
2.Phạm vi sản phẩm
DiamondShopSystem đóng vai trò là cầu nối quan trọng giữa Công ty và khách hàng trên toàn quốc, tận dụng sức mạnh của Internet để tiếp cận và phục vụ người tiêu dùng mọi lúc, mọi nơi. Website không chỉ hỗ trợ quảng bá thương hiệu và giới thiệu sản phẩm mà còn thu thập ý kiến phản hồi từ khách hàng. Những dữ liệu này sẽ giúp Công ty cải thiện chất lượng sản phẩm, dịch vụ và định hình chiến lược kinh doanh trong tương lai.
    II. Mô tả Tổng Quát
1. Chức năng
1.1 Chức năng dành cho khách hàng vãng lai (Guest):

2.1
Xem thông tin về cửa hàng. Xem và tìm kiếm thông tin về sản phẩm (kim cương).
2.1.1
Xem thông tin về cửa hàng: Fanpage, mạng xã hội, hotline, Fax, địa chỉ, và các thông tin giới thiệu khác.
2.1.2
Tạo tài khoản để mua hàng.
2.1.3
Xem danh sách các mẫu kim cương mới cập nhật, các mẫu kim cương bán chạy nhất ( có số lượng mua nhiều nhất).
2.1.4
Xem danh sách kim cương theo từng danh mục (ví dụ: loại kim cương, kiểu dáng, kích thước…).
2.1.5
Xem chi tiết mô tả kim cương và các sản phẩm kim cương tương tự trong doanh mục (xem video, hình ảnh nội dung mô tả chi tiết về sản phẩm kim cương)
2.1.6
Xem đánh giá và bình luận của khách hàng khác về sản phẩm kim cương
2.1.7
Lọc, tìm kiếm kim cương nâng cao (dựa theo tên, mã sản phẩm, giá cả (tăng dần, giảm dần…), loại, kiểu dáng, chất lượng, hoặc thương hiệu)
2.1.8
Đọc tin tức về thị trường kim cương (giá cả, xu hướng, sự kiện lớn).
2.1.9
Xem các chương trình khuyến mãi, giảm giá dành cho khách hàng.
2.1.10
Xem quy trình kiểm định chất lượng kim cương tại cửa hàng (hình ảnh, video minh họa).
2.1.11
Xem chính sách bảo hành, đổi trả sản phẩm.
2.1.12


Xem vị trí cửa hàng trên bản đồ.







1.2 Chức năng dành cho khách hàng (Customer): ngoài các chức năng như một Guest, đối tượng Customer được bổ sung các chức năng sau:


2.2
Quản lý giỏ hàng (Shoppingcart)
2.2.1
Thêm sản phẩm vào giỏ hàng. Lưu các thông tin như: Tên sản phẩm, mã sản phẩm, giá, số lượng, thuộc tính kim cương(loại kim cương, carat, màu sắc, độ trong, vết cắt,..)
2.2.2
Xóa sản phẩm khỏi giỏ hàng
2.2.3
Xem chi tiết giỏ hàng(danh sách các sản phẩm, số lượng, giá từng sản phẩm, tổng số tiền của từng loại sản phẩm)
2.2.4
Xem thông tin tóm tắt (tên sản phẩm, số mặt hàng, tổng tiền) của giỏ hàng



2.3
Quản lý hóa đơn (Order)
2.3.1
Tạo hóa đơn dựa trên các mục đã lưu trong giỏ hàng(bao gồm thông tin khách hàng, chi tiết sản phẩm, giá từng loại sản phẩm, mã giảm giá, phí VAT, tổng tiền, phương thức thanh toán, thời gian tạo hóa đơn)
2.3.2
Lưu hóa đơn đã tạo
2.3.3
Hủy hóa đơn
2.3.4
Xem thông tin lịch sử giao dịch(thời gian, tổng tiền, trạng thái thanh toán).
2.3.5
Gửi thông tin phản hồi về sản phẩm và chất lượng dịch vụ ( nội dung phản hồi, đánh giá số sao, ảnh minh họa nếu có)



2.4
Quản lý tài khoản (Account)
2.4.1
Cập nhật thông tin tài khoản(Tên, số điện thoại, địa chỉ, email, mật khẩu,..)





1.3 Chức năng dành cho nhân viên (Employee): Các nhân viên được phân nhóm theo vai trò (Role), bao gồm: Sales Staff, Delivery Staff, Manager và Admin. Từng vai trò có quyền hạn khác nhau khi tương tác với hệ thống.


3.1
Sales Staff (Nhân viên bán hàng)
3.1.1
Hỗ trợ khách hàng trong quá trình mua hàng tại cửa hàng hoặc trực tuyến 
3.1.2
Xem thông tin đơn hàng mới cho khách hàng
3.1.3
Tạo đơn hàng mới cho khách hàng 
3.1.4
Áp dụng chương trình khuyến mãi và tính toán giá
3.1.5
Cập nhật trạng thái đơn hàng (ví dụ: đã thanh toán)
3.1.6
Tra cứu thông tin khách hàng 
3.1.7
Quản lý tài khoản cá nhân
3.2
Delivery Staff (Nhân viên giao hàng)
3.2.1
Quản lý và giao các đơn hàng kim cương đến khách hàng
3.2.2
Xem danh sách đơn hàng cần giao và đã được giao(bao gồm: địa chỉ, số điện thoại, giá trị đơn hàng)
3.2.3
Cập nhật trạng thái đơn hàng (ví dụ: đang giao, giao thành công, giao thất bại)
3.2.4
Báo cáo đơn hàng không giao được(kèm lý do)
3.2.5
Quản lý tài khoản cá nhân
3.3
Manager (Quản lý cửa hàng)
3.3.1
Theo dõi và điều phối hoạt động hàng ngày tại cửa hàng kim cương
3.3.2
Quản lý nhân viên  bán hàng và giao hàng
3.3.3
Quản lý giá sản phẩm hoặc áp dụng chương trình khuyến mãi
3.3.4
Xem và phân tích báo cáo doanh thu, hàng tồn kho và hiệu suất bán hàng
3.3.5
Quản lý thông tin khách hàng VIP hoặc lịch sử mua hàng
3.3.6
Xem thông tin chi tiết khách hàng
3.3.7
Theo dõi trạng thái đơn hàng và can thiệp khi cần
3.3.8
Quản lý tài khoản cá nhân
3.4
Admin (Quản trị hệ thống)
3.4.1
Duy trì và quản lý toàn bộ hệ thống quản lý cửa hàng kim cương
3.4.2
Thêm, xóa, hoặc cập nhật tài khoản nhân viên và vai trò tương ứng
3.4.3
Sao lưu, khôi phục dữ liệu, và quản lý nhật ký hoạt động
3.4.5
Theo dõi toàn bộ hoạt động trong hệ thống, bao gồm lịch sử đơn hàng và chỉnh sửa dữ liệu
3.4.6
Quản lý tài khoản cá nhân










2. Phân loại Người dùng
Các đối tượng tương tác với hệ thống gồm: Guest, Customer, Admin và Employee( bao gồm Sales Staff, Delivery Staff và  Manager) Được thể hiện trên sơ đồ sau:

Hình 1: Các actor của hệ thống
3. Môi trường thiết kế & xây dựng
	Website được xây dựng bao gồm:
-      Django framework.
-        Cơ sở dữ liệu SQL Server/MySQL  (phiên bản từ 2008 trở lên)
-   	Đảm bảo hoạt động tốt trên các trình duyệt phổ biến như: Chrome, Firefox, Safari, Internet Explorer.
-        Đảm bảo hoạt động tốt trên nhiều loại thiết bị khác nhau: Computer, Smartphone, IPAD


    III.  Yêu Cầu Tương tác Ngoài
1.Giao diện người dùng
+Giao diện không quá phức tạp, tránh sử dụng quá nhiều màu sắc gây rối mắt.
+Sử dụng tông màu sang trọng (như trắng, vàng ánh kim, đen) để phù hợp với lĩnh vực kinh doanh kim cương.

2.Yêu cầu tương tác với phần cứng
+Hiện tại hệ thống chưa cần tương tác với các thiết bị đặc biệt khác ngoài hệ thống máy tính thông thường.

3.Yêu Cầu tương tác với phần mềm
	+Trong tương lai dữ liệu hóa đơn của hệ thống cần trích xuất sang cho hệ thống kê toán của Công ty.


    IV. Kiến Trúc hệ thống
	IV.1 Kiến trúc Tổng Thể của hệ Thống

Hình 2: Component diagram


Hình 3: Deployment diagram


Hình 4: class diagram
	IV.2 Chi tiết các thành phần
	IV.2.1 Front End
	Biểu đồ use-case biểu diễn sự tương tác của khách vãng lai (Guest) với hệ thống:

            				Hình 5: Hình use-case của Guest
Biểu đồ use-case biểu diễn sự tương tác của khách hàng ( Customer) với hệ thống:

Hình 6: Hình use-case của Customer
IV.2.2 Back End
Biểu đồ use-case thể hiện sự thao tác của Admin đối với hệ thống:

   			 Hình 7: Admin use-case diagram
Biểu đồ use-case biểu diễn thao tác quản lý nhân viên:

   			Hình 8: use-case quản lý nhân viên
Biểu đồ activity thể hiện thao tác thêm nhân viên mới:

 	Hình 9: Activity diagram thêm nhân viên


	Biểu đồ tuần tự (sequence) thể hiện thao tác thêm nhân viên mới:

Hình 10: Sequence diag thêm nhân viên


 Hình 11 Sequence diag thêm sản phẩm

   V. Yêu cầu phi chức năng
- Hệ thống cần đảm bảo sẵn sàng hoạt động 24/7.
- Cơ sở dữ liệu của hệ thống luôn được backup vào mỗi ngày cuối cùng của tháng một cách tự động.
- Hệ thống được xây dựng hoàn toàn miễn phí.
 -Hệ thống cần tương thích với các thiết bị và trình duyệt phổ biến, hỗ trợ cả trên máy tính và thiết bị di động.
-Giao diện thân thiện, dễ sử dụng và dễ thao tác đối với người dùng.
- Về mặt an toàn:
+Các thông tin mật khẩu cần được mã hóa theo chuẩn hiện hành (MD5, RSA).
+Hệ thống không bị ảnh hưởng bởi các tấn công thông thường như SQL Injection

    VI. Các yêu cầu khác
-Hệ thống thông báo: Gửi thông báo qua email hoặc ứng dụng khi có sự kiện quan trọng (hết hàng, bảo trì hệ thống, các chương trình khuyến mãi,....).

    VII. Phục Lục








		
