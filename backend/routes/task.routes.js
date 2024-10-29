import express from 'express';
import { createTask, getTasks} from '../controllers/task.controllers.js';
import { verifyApiKey } from '../middleware/validateApi.js';

const router = express.Router();

router.get('/getTasks', getTasks);
router.post('/createTasks', verifyApiKey, createTask);



export default router;