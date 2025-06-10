 
// ------------------MANEJO DE DATOS CON JSON Y ASYNC/AWAIT------------------------

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

import mysql from 'mysql2/promise';

export interface User {
    id: string;
    name: string;
    age: number;
}

const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: '', 
    database: 'usuario_express'
});

export async function createUser(name: string, age: number): Promise<User> {
    const [result]: any = await pool.query(
        'INSERT INTO usuario (nombre, edad) VALUES (?, ?)',
        [name, age]
    );
    const id = result.insertId;
    return { id, name, age };
}

export async function listUsers(): Promise<User[]> {
    const [rows]: any = await pool.query('SELECT id, nombre as name, edad as age FROM usuario');
    return rows;
}

export async function getUserById(id: string): Promise<User | undefined> {
    const [rows]: any = await pool.query('SELECT id, nombre as name, edad as age FROM usuario WHERE id = ?', [id]);
    return rows[0];
}

export async function updateUserName(id: string, newName: string): Promise<void> {
    await pool.query('UPDATE usuario SET nombre = ? WHERE id = ?', [newName, id]);
}