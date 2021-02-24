def count_down(number):
    if number < 0:  # 재귀함수를 돌릴 때는 언제 재귀함수가 끝날지 알려줘야지 무한루프에 빠지지 않음! (탈출조건에 대한 고민)
        return
    print(number)  # number를 출력하고

    # count_down 함수를 number - 1 인자를 주고 다시 호출한다! (자기가 자기를 부르고 있음)
    # 재귀함수는 자기 자신을 호출함으로써 코드를 간결하고 명확하게 만들 수 있다는 장점이 있다.
    count_down(number - 1)


count_down(60)