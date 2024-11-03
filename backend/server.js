import dotenv from 'dotenv';
import express from 'express';
import connectToDatabase from './db/connect.js';
import taskRoutes from './routes/task.routes.js';
import agentRoutes from './routes/agent.routes.js';



const PORT = process.env.PORT || 2000;

// Configuration for the app
const app = express();


dotenv.config();
app.use(express.json());

app.use('/api/tasks/', taskRoutes);
app.use('/api/agents/', agentRoutes);


const startServer = () =>{
    app.listen(PORT, () => {
        connectToDatabase();
        console.log(`Server is running on port ${PORT}`);
    });
}


export {app, startServer};

startServer();