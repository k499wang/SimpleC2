import dotenv from 'dotenv';

dotenv.config();

export const verifyApiKey = (req, res, next) => {
    const apiKey = req.headers['x-api-key'];

    if(apiKey === process.env.SECRET_API_KEY){
        next();
    } else {
        res.status(403).json({message: 'Forbidden'});
    }
}

