# 1113 Homework

## 1번

- F
- T
- F
- T



## 2번

action은 공개적 처리나 복잡한 처리를 행할 때를 위한 public한 method로 mutation을 호출한다. mutation은 state의 변경을 위한 메소드이다. mutation은 동기적인 처리이고 action은 비동기적 처리도 가능하다. 이는 mutation에서 state의 변경이 비동기적으로 수행되었을 경우 예측 불가능한 상태가 되는 것을 막기위한 의도가 있다.



## 3번

(a) :  Vuex.store

(b) : state.count+=1

(c) : context.commit('increment')