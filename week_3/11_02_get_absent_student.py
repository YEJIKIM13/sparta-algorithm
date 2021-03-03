all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    # dictionary 에 all_student 를 전부 넣고 present_student 를 돌면서 그 키가 존재하는지 여부에 따라서 키를 제거하고
    # 마지막까지 키가 없어지지 않았다면 출석하지 않은 것!
    student_dict = {}
    for key in all_array:
        student_dict[key] = True  # 키를 이용해서 저장하고 삭제한 것이기 때문에 아무 값이나 넣어도 상관없음

    # 출석한 학생들 하나씩 제거
    for key in present_array:
        del student_dict[key]

    # 남은 키 하나 반환
    for key in student_dict.keys():  # 딕셔너리에서 키 반환하는 메소드
        return key


print(get_absent_student(all_students, present_students))