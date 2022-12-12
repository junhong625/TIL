function foo() {
    globalVariable = 123;
    var localVariable = 456;
    console.log(this === global);
    console.log(this.globalVariable);
    console.log(localVariable);
  }
  
  foo();
  console.log(globalVariable);
//   console.log(localVariable);