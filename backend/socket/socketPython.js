import net from 'net';

const socketPython = new net.Socket();

// Connecting to the python server
socketPython.connect(9999, '127.0.0.1', () => {
    console.log("Connected to Server")
});

// Handle errors
socketPython.on('error', (error) => {
    console.error('Socket error:', error);
    setTimeout(() => {
        console.log('Attempting to reconnect...');
        socketPython.connect(9999, '127.0.0.1', () => {
            console.log("Reconnected to Server");
        });
    }, 5000); // Retry after 5 seconds
});

// Handle closure
socketPython.on('close', () => {
    console.log('Connection to server closed');
});

export default socketPython;