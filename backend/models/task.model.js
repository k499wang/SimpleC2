import mongoose from 'mongoose';

const taskSchema = new mongoose.Schema({
    command: {
        type: String,
        required: true
    },
    
    agentId:{
        type: String, // this means that the senderId will be an ObjectId from MongoDB
        required: true,
    },

    arguments:{
        type: String,
        default: ""
    },

    status:{
        type: String,
        default: 'pending'
    },

    priority:{
        type: String,
        default: 'low'
    },

    output:{
        type: String,
        default: 'Not Finished'
    },

    createdAt: {
        type: Date,
        default: Date.now,
      },

    completedAt: {
        type: Date,
      },


});

const Task = mongoose.model('Task', taskSchema);
export default Task;