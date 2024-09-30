(function() {
  const socket = new WebSocket('ws://localhost:3000');

  socket.onopen = function() {
      console.log('Connected to hot reload server');
  };

  socket.onmessage = function(event) {
      const data = JSON.parse(event.data);
      if (data.type === 'reload') {
          console.log('Reloading page...');
          window.location.reload();
      }
  };

  socket.onclose = function() {
      console.log('Disconnected from hot reload server');
      // Try to reconnect every 5 seconds
      setTimeout(() => {
          console.log('Attempting to reconnect...');
          window.location.reload();
      }, 5000);
  };
})();