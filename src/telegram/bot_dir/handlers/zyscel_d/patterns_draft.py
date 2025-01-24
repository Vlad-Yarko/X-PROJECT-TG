# from re import compile, IGNORECASE
#
# c = ""
#
# # pattern1 = compile(r"\n?..?(ПРОДАНо)..?\s{2}([\w ,()-][^\n]+)\s{2}.. ?([\w ,()-][^\n]+)\n{2}~~~[\w ,()-][^:]+..([\w ,()-][^\n]+)~~~\n([\w ,()-][^\n]*)~~~\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)", IGNORECASE)
# # pattern2 = compile(r"\n?([\w ,()-][^\n]+)\n{2}.. ?([\w ,()-][^\n]+)\n{2}[\w ,()-]+: ?([\w ,()-]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)~~~\n([\w ,()-][^\n]*)\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)", IGNORECASE)
# # pattern3 = compile(r"\n?..?(ПРОДАНо)..?\n{2}([\w ,()-][^\n]+)\n{2}.. ?([\w ,()-][^\n]+)\n{2}[\w ,()-]+: ?([\w ,()-]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)", IGNORECASE)
# # pattern4 = compile(r"\n?([\w ,()-][^\n]+)\n{2}.. ?([\w ,()-][^\n]+)\n{2}[\w ,()-]+: ?([\w ,()-]*)~~~\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)", IGNORECASE)
# # pattern5 = compile(r"\n?([\w ,()-][^\n]+)\s{2}.. ?([\w ,()-][^\n]+)\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)\n[\w ,()-][^:]+..([\w ,()-][^\n]*)\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)", IGNORECASE)
# # pattern6 = compile(r"\n?([\w ,()-][^\n]+)\n{2}.. ?([\w ,()-][^\n]+)\n{2}[\w ,()-]+: ?([\w ,()-]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}\w[^:]+..(\w[^\n]+)", IGNORECASE)
# # pattern7 = compile(r"\n?..?(ПРОДАНо)..?\n{2}([\w ,()-][^\n]+)\n{2}.. ?([\w ,()-][^\n]+)\n{2}[\w ,()-]+: ?([\w ,()-]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}\w[^:]+..(\w[^\n]+)", IGNORECASE)
# # pattern8 = compile(r"\n?..?(ПРОДАНо)..?\n{2}([\w ,()-][^\n]+)\n{2}.. ?([\w ,()-][^\n]+)\n{2}[\w ,()-]+: ?([\w ,()-]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)", IGNORECASE)
# # pattern9 = compile(r"\n?([\w ,()-][^\n]+)\n{2}.. ?([\w ,()-][^\n]+)\n{2}[\w ,()-]+: ?([\w ,()-\\]*)\n{2}[\w ,()-\\][^:]+..([\w ,()-][^\n]+)\n{2}([\w ,()-]+(?:\n[\w+,()-]+)?)", IGNORECASE)
# # pattern10 = compile(r"\n?..?(ПРОДАНо)..?\n{2}([\w ,()-][^\n]+)\n{2}.. ?([\w ,()-][^\n]+)\n{2}[\w ,()-]+: ?([\w ,()-\\]*)\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)\n{2}([\w ,()-]+(?:\n[\w+,()-]+)?)", IGNORECASE)
# # pattern11 = compile(r"\n?([\w ,()-][^\n]+)\n{2}.. ?([\w ,()-][^\n]+)\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)", IGNORECASE)
# # pattern12 = compile(r"\n?..?(ПРОДАНо)..?\n{2}([\w ,()-][^\n]+)\n{2}.. ?([\w ,()-][^\n]+)\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)", IGNORECASE)
#
#
#
# prodano = r"..?(ПРОДАНо)..?\s{2}"
# title = r"([\w ,()-][^\n]+)\s{2}"
# state = r".. ?([\w ,()-][^\n]+)\n{2}"
# size = r"[\w ,()-\\]+: ?([\w ,()-\\]*)"
# add_size = r"([\w ,()-][^\n]*)"
# five_add_size = r"([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)"
# four_add_size = r"([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)"
# double_add_size = r"([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)"
# double_add_size_price = r"\n{2}([\w ,()-]+(?:\n[\w+,()-]+)?)"
# price = r"\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)"
#
# pattern1 = compile(r"\n?" + prodano + title + state + size + r"\n" + add_size + price, IGNORECASE)
# pattern2 = compile(r"\n?" + title + state + size + r"\n" + double_add_size + r"\n{2}" + four_add_size + price,
#                    IGNORECASE)
# pattern3 = compile(r"\n?" + prodano + title + state + size + r"\n" + double_add_size + r"\n{2}" + four_add_size + price,
#                    IGNORECASE)
# pattern4 = compile(r"\n?" + title + state + size + r"\n" + double_add_size + r"\n{2}" + five_add_size + price,
#                    IGNORECASE)
# pattern5 = compile(r"\n?" + title + state + size + r"\n" + add_size + price, IGNORECASE)
# pattern6 = compile(
#     r"\n?" + title + state + size + r"\n" + double_add_size + r"\n{2}" + five_add_size + r"\n{2}" + five_add_size + price,
#     IGNORECASE)
# pattern7 = compile(
#     r"\n?" + prodano + title + state + size + r"\n" + double_add_size + r"\n{2}" + five_add_size + r"\n{2}" + five_add_size + price,
#     IGNORECASE)
# pattern8 = compile(r"\n?" + prodano + title + state + size + r"\n" + double_add_size + r"\n{2}" + five_add_size + price,
#                    IGNORECASE)
# pattern9 = compile(r"\n?" + title + state + size + price + double_add_size_price, IGNORECASE)
# pattern10 = compile(r"\n?" + prodano + title + state + size + price + double_add_size_price, IGNORECASE)
# pattern11 = compile(r"\n?" + title + state + price, IGNORECASE)
# pattern12 = compile(r"\n?" + prodano + title + state + price, IGNORECASE)
#
#
# is_not_available_pattern = compile(r"\n?" + prodano, IGNORECASE)
#
# try:
#     if is_not_available_pattern.match(c):
#
#         product = pattern1.match(c)
#
#         if product:
#
#             print(product.group(1))
#             print(product.group(2))
#             print(product.group(3))
#             print(product.group(4))
#             print(product.group(5))
#             print(product.group(6))
#
#         else:
#
#             product = pattern7.match(c)
#
#             if product:
#
#                 print(product.group(1))
#                 print(product.group(2))
#                 print(product.group(3))
#                 print(product.group(4))
#                 print(product.group(5))
#                 print(product.group(6))
#                 print(product.group(7))
#                 print(product.group(8))
#                 print(product.group(9))
#                 print(product.group(10))
#                 print(product.group(11))
#                 print(product.group(12))
#                 print(product.group(13))
#                 print(product.group(14))
#                 print(product.group(15))
#                 print(product.group(16))
#                 print(product.group(17))
#
#
#
#             else:
#
#                 product = pattern3.match(c)
#
#                 if product:
#                     print(product.group(1))
#                     print(product.group(2))
#                     print(product.group(3))
#                     print(product.group(4))
#                     print(product.group(5))
#                     print(product.group(6))
#                     print(product.group(7))
#                     print(product.group(8))
#                     print(product.group(9))
#                     print(product.group(10))
#                     print(product.group(11))
#
#                 else:
#
#                     product = pattern8.match(c)
#
#                     if product:
#
#                         print(product.group(1))
#                         print(product.group(2))
#                         print(product.group(3))
#                         print(product.group(4))
#                         print(product.group(5))
#                         print(product.group(6))
#                         print(product.group(7))
#                         print(product.group(8))
#                         print(product.group(9))
#                         print(product.group(10))
#                         print(product.group(11))
#                         print(product.group(12))
#
#                     else:
#                         product = pattern10.match(c)
#
#                         if product:
#
#                             print(product.group(1))
#                             print(product.group(2))
#                             print(product.group(3))
#                             print(product.group(4))
#                             print(product.group(5))
#                             print(product.group(6))
#
#                         else:
#
#                             product = pattern12.match(c)
#
#                             if product:
#                                 print(product.group(1))
#                                 print(product.group(2))
#                                 print(product.group(3))
#                                 print(product.group(4))
#
#                             else:
#
#                                 print("KOKO")
#
#     else:
#
#         product = pattern2.match(c)
#
#         if product:
#
#             print(product.group(1))
#             print(product.group(2))
#             print(product.group(3))
#             print(product.group(4))
#             print(product.group(5))
#             print(product.group(6))
#             print(product.group(7))
#             print(product.group(8))
#             print(product.group(9))
#             print(product.group(10))
#
#         else:
#
#             product = pattern6.match(c)
#
#             if product:
#                 print(product.group(1))
#                 print(product.group(2))
#                 print(product.group(3))
#                 print(product.group(4))
#                 print(product.group(5))
#                 print(product.group(6))
#                 print(product.group(7))
#                 print(product.group(8))
#                 print(product.group(9))
#                 print(product.group(10))
#                 print(product.group(11))
#                 print(product.group(12))
#                 print(product.group(13))
#                 print(product.group(14))
#                 print(product.group(15))
#                 print(product.group(16))
#
#             else:
#
#                 product = pattern5.match(c)
#
#                 if product:
#
#                     print(product.group(1))
#                     print(product.group(2))
#                     print(product.group(3))
#                     print(product.group(4))
#                     print(product.group(5))
#
#                 else:
#
#                     product = pattern4.match(c)
#
#                     if product:
#                         print(product.group(1))
#                         print(product.group(2))
#                         print(product.group(3))
#                         print(product.group(4))
#                         print(product.group(5))
#                         print(product.group(6))
#                         print(product.group(7))
#                         print(product.group(8))
#                         print(product.group(9))
#                         print(product.group(10))
#                         print(product.group(11))
#
#                     else:
#
#                         product = pattern9.match(c)
#
#                         if product:
#                             print(product.group(1))
#                             print(product.group(2))
#                             print(product.group(3))
#                             print(product.group(4))
#                             print(product.group(5))
#
#                         else:
#
#                             product = pattern11.match(c)
#
#                             if product:
#                                 print(product.group(1))
#                                 print(product.group(2))
#                                 print(product.group(3))
#
#                             else:
#
#                                 print("LOLO")
#
#     print('----------------------------------')
#
# # product = False
# #
# # if product:
# #
# #         print(product.group(1))
# #         print(product.group(2))
# #         print(product.group(3))
# #         print(product.group(4))
# #         print(product.group(5))
# #         print(product.group(6))
# #
# #     else:
# #
# #         product = pattern7.match(c)
# #
# #         if product:
# #
# #             print(product.group(1))
# #             print(product.group(2))
# #             print(product.group(3))
# #             print(product.group(4))
# #             print(product.group(5))
# #             print(product.group(6))
# #             print(product.group(7))
# #             print(product.group(8))
# #             print(product.group(9))
# #             print(product.group(10))
# #             print(product.group(11))
# #             print(product.group(12))
# #             print(product.group(13))
# #             print(product.group(14))
# #             print(product.group(15))
# #             print(product.group(16))
# #             print(product.group(17))
# #
# #
# #
# #         else:
# #
# #             product = pattern3.match(c)
# #
# #             if product:
# #                 print(product.group(1))
# #                 print(product.group(2))
# #                 print(product.group(3))
# #                 print(product.group(4))
# #                 print(product.group(5))
# #                 print(product.group(6))
# #                 print(product.group(7))
# #                 print(product.group(8))
# #                 print(product.group(9))
# #                 print(product.group(10))
# #                 print(product.group(11))
# #
# #             else:
# #
# #                 product = pattern8.match(c)
# #
# #                 if product:
# #
# #                     print(product.group(1))
# #                     print(product.group(2))
# #                     print(product.group(3))
# #                     print(product.group(4))
# #                     print(product.group(5))
# #                     print(product.group(6))
# #                     print(product.group(7))
# #                     print(product.group(8))
# #                     print(product.group(9))
# #                     print(product.group(10))
# #                     print(product.group(11))
# #                     print(product.group(12))
# #
# #                 else:
# #                     product = pattern10.match(c)
# #
# #                     if product:
# #
# #                         print(product.group(1))
# #                         print(product.group(2))
# #                         print(product.group(3))
# #                         print(product.group(4))
# #                         print(product.group(5))
# #                         print(product.group(6))
# #
# #                     else:
# #
# #                         product = pattern12.match(c)
# #
# #                         if product:
# #                             print(product.group(1))
# #                             print(product.group(2))
# #                             print(product.group(3))
# #                             print(product.group(4))
# #
# #                         else:
# #
# #                             print("KOKO")
# #
#
# prodano = r"..?(ПРОДАНо)..?\s\s?"
#     title = r"([\w ,()-][^\n]+)\s{2}"
#     state = r".. ?([\w ,()-][^\n]+)\n{2}"
#     size = r"[\w ,()-\\]+: ?([\w ,()-\\]*)"
#     add_size = r"([\w ,()-][^\n]*)"
#     five_add_size = r"([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)"
#     four_add_size = r"([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)\n([\w ,()-][^\n]*)"
#     double_add_size = r"([\w ,()-][^\n]*(?:\n[\w ,()-][^\n]*)?)"
#     double_add_size_price = r"\n{2}([\w ,()-]+(?:\n[\w+,()-]+)?)"
#     price = r"\n{2}[\w ,()-][^:]+..([\w ,()-][^\n]+)"
#
#     # pattern2 = compile(r"\n?" + title + state + size + r"\n" + double_add_size + r"\n{2}" + four_add_size + price, IGNORECASE)
#     # pattern4 = compile(r"\n?" + title + state + size + r"\n" + double_add_size + r"\n{2}" + five_add_size + price, IGNORECASE)
#     # pattern5 = compile(r"\n?" + title + state + size + r"\n" + add_size + price, IGNORECASE)
#     # pattern6 = compile(r"\n?" + title + state + size + r"\n" + double_add_size + r"\n{2}" + five_add_size + r"\n{2}" + five_add_size + price, IGNORECASE)
#     # pattern9 = compile(r"\n?" + title + state + size + price + double_add_size_price, IGNORECASE)
#     # pattern11 = compile(r"\n?" + title + state + price, IGNORECASE)
#
#     is_not_available_pattern = compile(r"\n?" + prodano, IGNORECASE)