'''
동물들 이름이 랜덤으로 0.5초 나오고 user가 정답 맞추는 프로그램을 구현하시오.
hint)
from time import sleep
sleep(0.5)->사용하면 0.5초 정지

동물들 list
li=['고양이', '강아지', '거북이', '토끼', '뱀', '사자', '호랑이', '표범', '치타', '하이에나', '기린', '코끼리', '코뿔소', '하마', '악어', '펭귄', '부엉이', '올빼미', '곰', '돼지', '소', '닭', '독수리', '타조', '고릴라', '오랑우탄', '침팬지', '원숭이', '코알라', '캥거루', '고래', '상어', '칠면조', '직박구리', '쥐', '청설모', '메추라기', '앵무새', '삵', '스라소니', '판다', '오소리', '오리', '거위', '백조', '두루미', '고슴도치', '두더지', '우파루파', '맹꽁이', '너구리', '개구리', '두꺼비', '카멜레온', '이구아나', '노루', '제비', '까치', '고라니', '수달', '당나귀', '순록', '염소', '공작', '바다표범', '들소', '박쥐', '참새', '물개', '바다사자', '살모사', '구렁이', '얼룩말', '산양', '멧돼지', '카피바라', '도롱뇽', '북극곰', '퓨마', '미어캣', '코요테', '라마', '딱따구리', '기러기', '비둘기', '스컹크', '돌고래', '까마귀', '매', '낙타', '여우', '사슴', '늑대', '재규어', '알파카', '양', '다람쥐', '담비']


ex)
동물들 이름으로 타자 게임
1.게임시작        
2.최고기록        
3.종료
>>>1

->
돼지 (0.5초 동안 보여주고 사라짐)

->
정답>>> 돼지
.
.
.
.
정답>>>산양
총 정답수:9

->
동물들 이름으로 타자 게임
1.게임시작        
2.최고기록        
3.종료
>>>2
최고기록은 9번입니다.
'''




# from random import randrange
# import os
# from time import sleep
# li=['고양이', '강아지', '거북이', '토끼', '뱀', '사자', '호랑이', '표범', '치타', '하이에나', '기린', '코끼리', '코뿔소', '하마', '악어', '펭귄', '부엉이', '올빼미', '곰', '돼지', '소', '닭', '독수리', '타조', '고릴라', '오랑우탄', '침팬지', '원숭이', '코알라', '캥거루', '고래', '상어', '칠면조', '직박구리', '쥐', '청설모', '메추라기', '앵무새', '삵', '스라소니', '판다', '오소리', '오리', '거위', '백조', '두루미', '고슴도치', '두더지', '우파루파', '맹꽁이', '너구리', '개구리', '두꺼비', '카멜레온', '이구아나', '노루', '제비', '까치', '고라니', '수달', '당나귀', '순록', '염소', '공작', '바다표범', '들소', '박쥐', '참새', '물개', '바다사자', '살모사', '구렁이', '얼룩말', '산양', '멧돼지', '카피바라', '도롱뇽', '북극곰', '퓨마', '미어캣', '코요테', '라마', '딱따구리', '기러기', '비둘기', '스컹크', '돌고래', '까마귀', '매', '낙타', '여우', '사슴', '늑대', '재규어', '알파카', '양', '다람쥐', '담비']
# best = -1
# while True:
#     os.system('cls')
#     print("동물들 이름으로 타자 게임")
#     print("1.게임시작")
#     print("2.최고기록")
#     print("3.종료")
#     n=input(">>>")
    
#     if n=='1':
#         cnt=0
#         i=0
#         while True:
#             i+=1
#             animal=li[randrange(1,100)]
#             os.system('cls')
#             print(animal)
#             sleep(0.5)
#             os.system('cls')
#             answer = input("정답>>>")
#             if animal == answer:
#                 cnt+=1
#             if i==10:
#                 if best < cnt:
#                     best =cnt
#                 print("총 정답수:",cnt)
#                 os.system('pause')
#                 break

#     elif n=='2':
#         if best == -1:
#             print("게임부터 시작하세요")
#         else:
#             print(f"최고기록은 {best}번 입니다.")
#         sleep(1)
#     elif n=='3':
#         print("프로그램이 종료됩니다.")
#         break
#     else:
#         print("잘 못 입력하셨습니다.")
#         sleep(1)