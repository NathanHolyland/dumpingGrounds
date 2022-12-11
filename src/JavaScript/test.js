function printNumbers(n) {
    let arr = [];
    for (let i = 0; i<=n; i++) {
      arr.push(i);
    }
    return arr;
  }
  
  function timesTables(x, n) {
    let arr = [];
    for (let i = 1; i<=n; i++) {
      arr.push(i*x);
    }
    return arr;
  }
  
  function arraySum(arr) {
    let sum = 0;
    arr.forEach(function add(a, b, c) {
      sum = sum + a;
    });
    return sum;
  }
  
  function reverseArray(arr) {
    let reversed = new Array();
    arr.forEach(function backPush(a, b, c) {
      reversed.unshift(a);
    });
    return reversed;
  }
  
  function numberSortArray(arr) { //rudementary bubble sort
    let change = true;
    while (change) {
      change = false
      for (let i=0; i<=arr.length; i++) {
        if (arr[i] > arr[i+1]) {
          let temp = arr[i+1];
          arr[i+1] = arr[i];
          arr[i] = temp;
          change = true
        }
      }
    }
    return arr
  }
  
  function elimNegatives(arr) {
    for (let i = 0; i<arr.length; i++) {
      if (arr[i] < 0) {
        arr.splice(i,1)
      }
    }
    return arr
  }
  
  function elimSpaces(str) {
    let x = str.replaceAll(/ */g,"")
    return x;
  }
  
  function countVowels(str) {
    
  }
  
  /*
  let x = [-1, 2, 5, -5];
  elimNegatives(x);
  console.log(x)
  */
  
  /*
  let x = "a a ahs aw yt asdh a "
  console.log(elimSpaces(x));
  */