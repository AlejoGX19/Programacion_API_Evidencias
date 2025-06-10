"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const asyncUserService_1 = require("./asyncUserService");
const app = (0, express_1.default)();
const PORT = 3000;
app.use(express_1.default.json());
app.post('/users', (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const { name, age } = req.body;
    if (!name || !age) {
        return res.status(400).send('Nombre y edad son requeridos');
    }
    const user = yield (0, asyncUserService_1.createUser)(name, age);
    res.status(201).json(user);
}));
app.get('/users', (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const users = yield (0, asyncUserService_1.listUsers)();
    res.json(users);
}));
app.get('/users/:id', (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const user = yield (0, asyncUserService_1.getUserById)(req.params.id);
    if (!user) {
        return res.status(404).send('Usuario no encontrado');
    }
    res.json(user);
}));
app.put('/users/:id', (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const { name } = req.body;
    if (!name) {
        return res.status(400).send('Nombre es requerido');
    }
    yield (0, asyncUserService_1.updateUserName)(req.params.id, name);
    const updated = yield (0, asyncUserService_1.getUserById)(req.params.id);
    res.json(updated);
}));
app.listen(PORT, () => {
    console.log(`Servidor escuchando en  http://localhost:${PORT}`);
});
