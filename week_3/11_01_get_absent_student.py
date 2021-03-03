all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    # 시간 복잡도 신경쓰지 않고 푼..
    # 우선 떠오르는 방법이 반복이지! 그게 나쁘다고는 할 수 없어, 비효율적일 뿐.
    for name in all_array:
        if name not in present_array:
            return name


print(get_absent_student(all_students, present_students))