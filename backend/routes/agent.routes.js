import express from 'express'
import { createAgent, registerAgent, getAgent, getAllAgents } from '../controllers/agent.controllers.js'
import { verifyApiKey } from '../middleware/validateApi.js';

const router = express.Router()

router.post('/register-agent', registerAgent);
router.post('/create-agent', verifyApiKey, createAgent);
router.get('/get-agent', verifyApiKey, getAgent);
router.get('/get-all-agents', verifyApiKey, getAllAgents
    
)

export default router;