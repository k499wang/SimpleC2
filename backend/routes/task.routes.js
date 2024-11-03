import express from 'express';
import { createTask, getTasks, updateTask} from '../controllers/task.controllers.js';
import { verifyApiKey } from '../middleware/validateApi.js';

const router = express.Router();

router.get('/getTasks', getTasks);
router.post('/createTasks', verifyApiKey, createTask);
router.post('/updateTasks', updateTask);



export default router;