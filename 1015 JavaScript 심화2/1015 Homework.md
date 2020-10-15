# 1015 Homework

## 1번.

- T
- F
- T



## 2번.

> console.log('Hello SSAFY')를 (1)로 setTimeout()의 결과를 (2)로, console.log('Bye SSAFY')를 (3)으로 칭한다.



Call stack에 (1)이 들어가고 실행되여 Console창에 표시된다. 이후 (2)가 스택에 들어가지만 함수를 완료하는데 시간이 걸리기 때문에 Call stack에서 나와 Web API에서 실행된다. 이 과정에서 (3)이 Call Stack에 들어가서 출력되어 Call Stack에서 나온다. Web API에서 실행된 (2)의 결과값은 Task Queue에 들어가 (3)이 완료되어 Call Stack에서 빠져나가 Call Stack이 비게되면, Event Loop가 실행되어 Task Queue에 있던 (2)의 함수 결과가 Call Stack에 들어가고 Console에 출력하고 Stack을 나가게 되어 모든 작업 공간이 비어 작업이 끝나게 된다.



## 3번.

```javascript
axios.get('---')
	.then(function(res){
    console.log('Hello SSAFY')
	})
	.then(function(res){
    setTimeout(function(){
        console.log('I am from setTimeout')
    },1000)
	})
	.then(function(res){
    console.log('Hello SSAFY')
	})
```



