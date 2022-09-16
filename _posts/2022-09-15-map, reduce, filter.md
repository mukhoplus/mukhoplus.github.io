---
layout: post
title: map, reduce, filter
excerpt: JavaScript는 정말..
date: 2022-09-15 15:29 +0000
last_modified_at: 2022-09-15 15:29:28 +0000
tags: [JavaScript]
toc:  true
---

JavaScript의 버전이 올라가면서 재미있는 요소들이 추가되었다고 합니다.

## 일반적인 Loop 구문

```javascript
let arr = [1, 2, 3, 5, 7, 9];

let new_arr1 = [];
for(let i=0; i<arr.length; ++i){
    if(arr[i] % 2 !== 0){
        new_arr1.push(arr[i]);
    }
}
console.log(new_arr1) // 1, 3, 5, 7, 9

let new_arr2 = [];
for(let a of arr){
    if(a % 2 !== 0){
        new_arr2.push(a);
    }
}
console.log(new_arr2) // 1, 3, 5, 7, 9

let new_arr3 = [];
arr.forEach((n) =>{
    if(n % 2 !== 0) new_arr3.push(n);
});
console.log(new_arr3) // 1, 3, 5, 7, 9

```

## map

- 요소를 일괄적으로 변경합니다.

```javascript
let arr = ['mukho', 'google'];
let new_arr = arr.map((v) => v.length);
console.log(new_arr); // [5, 6]
```

## filter

- 요소를 걸러내어 true/false로 반환합니다. 없으면 빈 배열을 반환합니다.

```javascript
let arr = [1, 2, 3, 5, 8, 9];
let new_arr = arr.filter((n) => (V % 2 === 0));
console.log(new_arr); // [2, 8]
```

## reduce

- reduce는 map, find, filter를 대체할 수 있습니다.
    - find는 조건에 맞는 값을 반환합니다. 단, 값이 여러 개라면 처음 찾은 값만 반환합니다.

```javascript
let arr = [9, 2, 8, 5, 7];
let sum = arr.reduce((pre, val) => pre + val);
console.log(sum); // 31

// map
var arr = ['foo', 'hello', 'diamond', 'A'];
var arr2 = arr.reduce((pre, value) => {
    pre.push(value.length);
    return pre;
}, []);
console.log(arr2); // [3, 5, 7, 1]

// filter
var arr = [4, 15, 377, 395, 400, 1024, 3000];
var arr2 = arr.reduce((pre, value) => {
    if (value % 5 == 0) {
        pre.push(value);
    }
    return pre;
}, []);
console.log(arr2); // [15, 395, 400, 3000]

// find
var arr = [4, 15, 377, 395, 400, 1024, 3000]
var arr2 = arr.reduce((pre, value) => {
    if (typeof pre == 'undefined' && value % 5 == 0) {
        pre = value;
    }
    return pre;
}, undefined);
console.log(arr2); // 15
```

## 기타 응용

```javascript
// 합집합
let arrA = [1, 4, 3, 2];
let arrB = [5, 2, 6, 7, 1];
console.log([...new Set([...arrA, ...arrB])]); // [1, 4, 3, 2, 5, 6, 7]

// 교집합
let arrC = [1, 4, 3, 2];
let arrD = [5, 2, 6, 7, 1];
console.log(arrC.filter(it => arrD.includes(it))) // [1, 2]
```

## 참고

- [ES6의 map, filter, reduce 정리](https://velog.io/@decody/map-%EC%A0%95%EB%A6%AC)
