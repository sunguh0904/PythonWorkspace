class ThailandPackege:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")
    __name__: str
if __name__ == "__main__":  # 좌항의 name의 우항의 main이면
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackege()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")