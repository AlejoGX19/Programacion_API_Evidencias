import express,  { Request, Response } from 'express';
import { createUser, listUsers, getUserById, updateUserName } from './asyncUserService';

const app = express();
const PORT = 3000;

app.use(express.json());

app.post('/users', async (req: Request, res: Response) => {
    const { name, age } = req.body;
    if (!name || !age) {
        return res.status(400).send('Nombre y edad son requeridos');
    }
    const user = await createUser(name, age);
    res.status(201).json(user);
});

app.get('/users', async (req: Request, res: Response) => {
    const users = await listUsers();
    res.json(users);
});

app.get('/users/:id', async (req: Request, res: Response) => {
    const user = await getUserById(req.params.id);
    if (!user) {
        return res.status(404).send('Usuario no encontrado');
    }
    res.json(user);
});

app.put('/users/:id', async (req: Request, res: Response) => {
    const { name } = req.body;
    if (!name) {
        return res.status(400).send('Nombre es requerido');
    }
    await updateUserName(req.params.id, name);
    const updated = await getUserById(req.params.id);
    res.json(updated);
});

app.listen(PORT, () => {
    console.log(`Servidor escuchando en  http://localhost:${PORT}`);
});