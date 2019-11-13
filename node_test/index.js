const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const cors = require('cors');
const PORT = process.env.PORT || 8000

app.use(cors());

app.get('/room/:name', function(req, res){
  const { name } = req.params;
  io.to(name).emit('chat message', 'api requested u')
return res.json({ message: 'Success' }).status(200);
});

app.get('/', function (req, res) {
  res.send('<h1>Hello world</h1>');
});

io.on('connection', function (socket) {
  console.log('a user connected with id %s', socket.id);

  socket.on('join', function (room) {
    socket.join(room);
    console.log(socket.id, "joined", room);
    io.to(room).emit("chat message", `You joined ${room}`);
  });

  socket.on('leave', function (room) {
    socket.leave(room);
    console.log(socket.id, "left", room);
  });

  // socket.on('chat message', function (data) {
  //   io.to(data.room).emit("chat message", data.message);
  // });

});

http.listen(PORT, function () {
  console.log(`listening on ${PORT}`);
});