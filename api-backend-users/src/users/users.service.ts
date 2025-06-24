import { Injectable } from '@nestjs/common';
import { User } from './user.entity';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';

@Injectable()
export class UsersService {
    constructor(@InjectRepository(User) private repo: Repository<User>) { }

    create(user: User){
        return this.repo.save(user);
    }

    findAll() {
        return this.repo.find();
    }

    findOne(id: number) {
        return this.repo.findOneBy({ id });
    }

    update(id: number, user: Partial<User>) {
        return this.repo.update(id, user);
    }

    remove(id: number) {
        return this.repo.delete(id);
    }
}
