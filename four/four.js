fetch('test.txt')
.then(response => response.text())
.then(text => console.log(text))