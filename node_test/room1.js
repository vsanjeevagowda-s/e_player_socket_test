const PORT = process.env.PORT || 8000
const socket = require('socket.io-client')(`http://localhost:${PORT}`);

socket.on('connect', function(){
  console.log('connect');
  socket.emit("join", 'room1');
});



socket.on('chat message', function(data){
  console.log(data)
});

socket.on('disconnect', function(){
  console.log('disconnect');
});