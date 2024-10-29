import mongoose from 'mongoose';

const agentSchema = new mongoose.Schema({
    agentId:{
        type: String,
        required: true,
        unique: true
    },

    userName:{
        type: String,
        default: "Not Known"
    },

    computerName:{
        type: String,
        default: "Not Known"
    },

    status:{
        type: String,
        default: 'inactive'
    },

    isCheckedIn:{
        type: Boolean,
        default: false
    },

    tasks: [{ 
        type: mongoose.Schema.Types.ObjectId, 
        ref: 'Task'
     }],

    os:{
        type: String,
        default: "Not Known"
    },

    ip:{
        type: String,
        default: "Not Known"
    },

    lastSeen:{
        type: Date,
        default: Date.now
    },

    registeredAt:{
        type: Date,
    }

});

const Agent = mongoose.model('Agent', agentSchema);
export default Agent;