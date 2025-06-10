"use strict";
// ------------------MANEJO DE DATOS CON JSON Y ASYNC/AWAIT------------------------
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
exports.createUser = createUser;
exports.listUsers = listUsers;
exports.getUserById = getUserById;
exports.updateUserName = updateUserName;
// import fs from 'fs/promises';
// import { v4 as uuidv4 } from 'uuid';
// export interface User {
//     id: string;
//     name: string;
//     age: number;
// }
// const FILE_PATH = './src/users.json';
// async function writeUsers(users: User[]): Promise<void> {
//     await fs.writeFile(FILE_PATH, JSON.stringify(users, null, 2));
// }
// export async function createUser(name: string, age: number): Promise<User> {
//     const users = await readUsers();
//     const newUser: User = {id: uuidv4(), name , age }; 
//     users.push(newUser);
//     await writeUsers(users);
//     return newUser;
// }
// export async function listUsers(): Promise<User[]> {
//     return await readUsers();
// }
// export async function getUserById(id: string): Promise<User | undefined> {
//     const users = await readUsers();
//     return users.find(user => user.id === id);
// }
// export async function updateUserName(id: string, newName: string): Promise<void> {
//     const users = await readUsers();
//     const user = users.find(u => u.id === id);
//     if (user) {
//         user.name = newName;
//         await writeUsers(users);
//     }
// }
// async function readUsers(): Promise<User[]> {
//     try {
//         const data = await fs.readFile(FILE_PATH, 'utf-8');
//         return JSON.parse(data);
//     } catch{
//         return [];
//     }
// }
//-------------------------------------------------------------------------------
// ------------------- MENEJO DE DATOS CON BASE DE DATOS ------------------------
// npm install mysql2
const promise_1 = __importDefault(require("mysql2/promise"));
// Configura tu conexión
const pool = promise_1.default.createPool({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'usuario_express'
});
function createUser(name, age) {
    return __awaiter(this, void 0, void 0, function* () {
        const [result] = yield pool.query('INSERT INTO usuario (nombre, edad) VALUES (?, ?)', [name, age]);
        const id = result.insertId;
        return { id, name, age };
    });
}
function listUsers() {
    return __awaiter(this, void 0, void 0, function* () {
        const [rows] = yield pool.query('SELECT id, nombre as name, edad as age FROM usuario');
        return rows;
    });
}
function getUserById(id) {
    return __awaiter(this, void 0, void 0, function* () {
        const [rows] = yield pool.query('SELECT id, nombre as name, edad as age FROM usuario WHERE id = ?', [id]);
        return rows[0];
    });
}
function updateUserName(id, newName) {
    return __awaiter(this, void 0, void 0, function* () {
        yield pool.query('UPDATE usuario SET nombre = ? WHERE id = ?', [newName, id]);
    });
}
