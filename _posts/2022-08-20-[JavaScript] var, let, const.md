---
layout: post
title: [JavaScript] var, let, const
date: 2022-08-20 16:20 +0000
last_modified_at: 2022-08-20 16:20:04 +0000
tags: [자바스크립트, CS]
toc:  true
---

## 들어가며

부스트캠프 챌린지 과정을 하면서 자연스럽게 자바스크립트에 제대로 입문을 하게 되었습니다. C++과 Python과는 다른 매력을 가진 언어였는데, 1주차에 var와 let의 차이에 대해 의문을 가졌었습니다. 그에 대해 따로 찾아본 내용을 정리해봤습니다.

## 변수

변수는 하나의 값을 저장하기 위해 확보한 메모리 공간 자체 또는 그 메모리 공간을 식별하기 위해 붙인 이름입니다. 예를 들어 이름 값을 저장하기 위해 주소가 '0000'인 공간을 사용한다면, 그 공간을 개발자가 쉽게 식별할 수 있게 이름을 붙여주는 것입니다. '서울특별시 종로구 ~'라는 주소에 '***의 집'이라는 이름을 붙여주는 것과 같습니다.
변수(variable)에 값을 저장하는 것을 **할당**(assignment), 변수에 저장된 값을 읽어 들이는 것을 **참조**(reference), 변수명을 자바스크립트 엔진에 알리는 것을 **선언**(declaration)이라고 합니다.

## 선언

자바스크립트의 선언에는 3가지 방법이 있습니다. let과 const는 ES6에서 추가된 키워드라고 합니다.

    1. var : 변수를 선언. 추가로 동시에 값을 초기화.
    2. let : 블록 스코프 지역 변수를 선언, 추가로 동시에 값을 초기화.
    3. const : 블록 스코프 읽기 전용 상수를 선언.

## 변수 선언

변수 선언은 아래 3가지 방법으로 가능합니다.

- ``var x = 11;``과 같이 ``var`` 키워드로 변수를 선언할 수 있습니다. 이 구문은 실행 맥락에 따라 **지역 및 전역 변수**를 선언하는데 모두 사용될 수 있습니다.
- ``let y = 22;``와 같이 ``const`` 또는 ``let``키워드로 변수를 선언할 수 있습니다. 이 구문은 블록 스코프 지역 변수를 선언하는데 사용될 수 있습니다.

``const``는 읽기 전용 상수를 만드는 키워드로, 스크립트가 실행 중인 동안 대입을 통해 값을 바꾸거나 재선언될 수 없습니다. ``const``는 변수의 선언과 초기화를 동시에 진행해야 합니다. 재할당의 금지가 곧 '불변'을 의미하지는 않습니다. ``(const) name = 'mukho'``처럼 원시값의 재할당은 불가능하지만, 객체 값의 재할당은 가능하기 때문입니다. 객체를 불변하게 하려면 ``Object.freeze()``를 사용해야 합니다.
그렇다면 ``var``와 ``let``의 차이는 무엇일까요?
- ``var`` 키워드
    - 변수의 중복 선언이 가능하여, 예기치 못한 값을 반환할 수 있음.
    - 함수 레벨 스코프로 인해 함수 외부에서 선언한 변수는 모두 전역 변수가 됨.
    - 변수 선언문 이전에 변수를 참조하면 언제나 undefined를 반환한다.
- ``let`` 키워드
    - 변수 중복 선언이 불가하다. 단, 재할당은 가능하다.
        
        ```javascript
        let name = 'mukho';
        console.log(name); // mukho

        // 중복 선언
        let name = 'muk'; // Uncaught SyntaxError: Identifier 'name' has already been declared.

        // 재할당
        name = 'muk';
        console.log(name); // muk
        ```
    
    - (const 포함) 코드 블록(함수, if, for, while, try/catch 등)을 지역 스코프로 인정하는 블록 레벨 스코프를 따른다.

        ```javascript
        let a = 1;
        if(true) let a = 2;
        console.log(a); // 1

        var b = 3;
        if(true) var b = 5;
        console.log(b); // 5
        ```

## 변수 할당

- 지정된 초기 값 없이 var 또는 let 문을 사용해서 선언된 변수는 ``undefined`` 값을 가집니다. 선언되지 않는 변수에 접근을 시도하는 경우 ``ReferenceError`` 예외가 발생합니다.

```javascript
var a;
console.log('a 값은 ' + a); // a 값은 undefined

console.log('b 값은 ' + b); // b 값은 undefined
var b;
// '변수 호이스팅'

console.log('c 값은 ' + c); // Uncaught ReferenceError: c is not defined

let x;
console.log('x 값은 ' + x); // x 값은 undefined

console.log('y 값은 ' + y); // Uncaught ReferenceError: y is not defined
let y;
```

## 호이스팅

위 예제 코드에서 선언되지 않은 var 변수 b에 먼저 접근했을 때 undefined가 출력되지만, 선언되지 않은 let 변수 y에 먼저 접근했을 때는 ReferenceError 예외가 발생했습니다.
왜 b는 선언되기 전에 접근했음에도 정상적으로 값에 접근할 수 있었을까요?

자바스크립트 변수의 특이한 점은 예외를 받지 않고도, 나중에 선언된 변수를 참조할 수 있다는 것입니다. 이를 호이스팅(hoisting)이라고 합니다. 자바스크립트 변수가 어떤 의미에서 함수나 문의 최상단으로 끌어올려지는 것입니다.
하지만, 끌어올려진 변수는 ``undefined`` 값을 반환합니다. 심지어 이 변수를 사용 또는 참조한 후에 선언 및 초기화를 하더라도 ``undefined`` 값을 반환합니다.

```javascript
console.log(x === undeinfed); // true
var x = 3;

var customVar = "value"
(function(){
    console.log(customVar); // undefined
    var customVar = "local value";
})
```

호이스팅이라는 개념 때문에, 함수 내의 모든 ``var`` 문은 가능한 함수 상단 근처에 두는 것이 좋습니다. 이것이 코드를 더욱 명확하게 해주기도 하니까요.

함수도 호이스팅됩니다. 단, 함수 선언(``function func(){}``)은 호이스팅이 되지만 함수 표현식(``var func = function(){}``)은 호이스팅되지 않습니다.

호이스팅 개념을 접하기 전부터 모든 변수와 함수는 최대한 위에 선언하는 버릇을 가지고 있었습니다. 그래서 처음 자바스크립트를 할 때 var를 썼음에도 큰 문제가 발생하지 않았던 것 같습니다.

## 참고

- [문법과 자료형](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types)
- [var, let, const의 차이 - 변수 선언 및 할당, 호이스팅, 스코프](https://www.howdy-mj.me/javascript/var-let-const/)
