import gspread

json_key_path = r'C:\Users\andol\Downloads\resolute-choir-355911-207bb94a8035.json'

gc = gspread.service_account(filename=json_key_path)
doc = gc.open("오답 노트")
sheet = doc.worksheet("시트1")


n = int(input('틀린 문제 수를 입력해주세요:'))

for i in range(n):
  question_number = input('틀린 문제의 번호를 입력해주세요:')
  your_answer = input('선택한 답을 입력해주세요:')
  right_answer = input('정답을 입력해주세요:')
  wrong_reason = input('틀린 이유를 입력해주세요:')

  image_path = f"C:\\Users\\andol\\OneDrive\\바탕 화면\\PythonWorkspace\\{question_number}.jpg"


  sheet.append_row([
    question_number,your_answer,right_answer,wrong_reason,image_path])


