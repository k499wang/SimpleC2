import Task from '../models/task.model.js';
import Agent from '../models/agent.model.js';


export const getTasks = async (req, res) => {
    try {
        const { agentId, status } = req.query;

        if(!agentId){
            return res.status(400).json({message: 'Agent ID is required'});
        }

        if (status == 'pending'){
            const tasks = await Task.find({agentId: agentId, status: 'pending'});
            res.status(200).json(tasks);
        }

        else if (status == 'completed'){
            const tasks = await Task.find({agentId: agentId, status: 'completed'});
            res.status(200).json(tasks);
        }
    
        else{
            const tasks = await Task.find({agentId: agentId});
            res.status(200).json(tasks);
        }
    }

    catch(error){
        res.status(500).json({message: error.message}); // Return a 500 status code and the error message
    }

}

export const updateTask = async(req, res) => {
    try{
        const {taskId, status, output, completedAt} = req.body;

        if(!taskId){
            return res.status(400).json({message: 'Task ID is required'});
        }

        const task = await Task.findById(taskId);

        if(!task){
            return res.status(404).json({message: 'Task not found'});
        }

        if (task.status == 'completed'){
            return res.status(400).json({message: 'Task is already completed'});
        }

        task.status = status || task.status;
        task.output = output || task.output;
        task.completedAt = completedAt || task.completedAt;

        await task.save();
        res.status(200).json(task);
    }

    catch(error){
        res.status(500).json({message: error.message});
    }
}

export const createTask = async (req, res) => {
    try{
        const {command, args, agentId, status, output, createdAt, completedAt} = req.body; // gets the ID field from the JSON

        if(!command || !agentId){
            return res.status(400).json({message: 'Command and Agent ID are required'});
        }

        // Checking if the agent exists
        const agent = await Agent.findOne({ agentId: agentId });

        if(!agent){
            return res.status(404).json({message: 'Agent not found'});
        }

        if(!agent.isCheckedIn) {
            return res.status(400).json({message: 'Agent is not checked in'});
        }
        

        const newTask = await Task.create({
            command,
            agentId,
            arguments: args || undefined,
            status: status || undefined,
            output: output || undefined,
            createdAt: createdAt || undefined,
            completedAt: completedAt || undefined
        });

        if(newTask){
            await newTask.save();
            res.status(201).json(newTask);
        }

        // push the task to the agent's task array
        agent.tasks.push(newTask._id);
        await agent.save();

    }

    catch(error){
        res.status(500).json({message: error.message});
    }

}