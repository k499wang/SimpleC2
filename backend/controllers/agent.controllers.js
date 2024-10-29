import Agent from '../models/agent.model.js';

export const createAgent = async (req, res) => {
    try{
        const {agentId} = req.body;
        const existingAgent = await Agent.findOne({ agentId: agentId });

        if(existingAgent) 
            return res.status(409).json({ message: 'Agent already exists' });

        if(!agentId)
            return res.status(400).json({message: 'Agent ID is required: ' + agentId});

        const newAgent = await Agent.create({agentId: agentId});

        return res.status(201).json(newAgent); // Return the created agent with a 201 status code
    }

    catch (error){
        res.status(500).json({message: error.message  });
    }
}

export const registerAgent = async (req, res) => {
    try{
        const {agentId, status, os, ip, lastSeen, isCheckedIn, computerName, userName} = req.body;

        // If the agent exists already
        const existingAgent = await Agent.findOne({ agentId: agentId });

        if (!existingAgent) 
            return res.status(409).json({ message: 'Agent does not exist in database' });

        if(existingAgent.isCheckedIn)
            return res.status(409).json({message: 'Agent is already checked in'});

        if(!agentId)
            return res.status(400).json({message: 'Agent ID and Availability is required'});
        

        existingAgent.status = status || existingAgent.status || "Unknown";
        existingAgent.os = os || existingAgent.os || "Unknown";
        existingAgent.ip = ip || existingAgent.ip || "Unknown";
        existingAgent.lastSeen = lastSeen || existingAgent.lastSeen || "Unknown";
        existingAgent.isCheckedIn = true;
        existingAgent.computerName = computerName || existingAgent.computerName || "Unknown";
        existingAgent.userName = userName || existingAgent.userName || "Unknown"; 


        await existingAgent.save();

        return res.status(201).json(existingAgent); // Return the created agent with a 201 status code
    }

    catch(error){
        res.status(500).json({message: error.message});
    }
}

export const getAgent = async (req, res) => {
    try{
        const {agentId} = req.body;
        const agent = await Agent.findOne({ agentId: agentId });
        if(!agent)
            return res.status(404).json({message: 'Agent not found' + agent});

        return res.status(200).json(agent);
    }

    catch(error){
        res.status(500).json({message: error.message});
    }
}

export const getAllAgents = async (req, res) => {
    try{
        const agents = await Agent.find({}, 'agentId');
        return res.status(200).json(agents);
    }
    catch(error){
        res.status(500).json({message: error.message});
    }
}
