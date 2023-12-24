create database prueba;
/*se crea la base de datos*/

use prueba;
/*para ocupar la base de datos prueba*/
create table Usuario
(
    id int,
    email varchar(255),
    username VARCHAR(50)
);

drop table Usuario;
/*elimina la tabla usuario*/

alter table Usuario add edad int;
/*agrega la columna edad*/

/*(1)*/
alter table Usuario add primary key(id);
/*establece la primary key*/

/*(2)*/
ALTER TABLE Usuario
MODIFY COLUMN id INT AUTO_INCREMENT;
/*el id se incrementa automaticamente*/

alter table Usuario drop column edad;
/*modifica la columna usuario*/
/*elimina la columna edad*/
alter table Usuario modify column email varchar
(50);
/*insertar registro*/
insert into Usuario
    (email, username)
values
    ('nicolas@correo.com', 'chanchitofeliz');
    
insert into Usuario
    (email, username, edad)
values
    ('andres@correo.com', 'chanchitotriste', 34);
    
insert into Usuario
    (email, username, edad)
values
    ('andres@correo.com', 'chanchitotriste', 34);
/*insertar en la tabla usuario en email y user name*/
UPDATE `prueba`.`usuario`
SET
`email` = 'carlito@gmail.com', `username` = 'carlitos' WHERE
(`id` = '1');
/*se les agrema el email el username y el id, el UPDATE que desea actualizar,
SET para especificar asignaciones a las columnas y valores, 
Where condicion es opcional pero importante*/
UPDATE `prueba`.`usuario`
SET
`username` = 'automovil' ,`email` = 'autoM@gmail.com'WHERE
(`id` = '3');
/*lo actualiza sin inportar el orden de los atributos*/
INSERT INTO usuario
    (id, email, username)
VALUES
    (3, 'auto@gmail.com', 'auto');
/*interta elemento inclullendo el id*/

DELETE FROM Usuario WHERE email = 'nicolas@correo.com'
LIMIT 1;
/*para elimanr el correo no me funciono por el id*/
UPDATE usuario
SET email = NULL;
-- SET username = NULL;
DELETE FROM usuario
WHERE email IS NULL;

/*otra alternativa*/
alter table Usuario add primary key(id);



ALTER TABLE Usuario
MODIFY COLUMN id INT AUTO_INCREMENT;
/*el id se incrementa automaticamente*/


select *
from Usuario;
/*nos muestra todo lo que contiene la tabla usuario * */

insert into Usuario
    (email, username)
values
    ('jack@correo.com', 'fchanchito');

select *
from Usuario
where email = 'jack@correo.com';
/*where nos permite filtrar las busquedas*/

UPDATE `prueba`.`usuario`
SET
`edad` = '25' WHERE
(`id` = '2');
/*se actualiza la edad*/

UPDATE `prueba`.`usuario`
SET
`username` = 'correosaavedra' WHERE
(`id` = '6');

insert into Usuario
    (email, username, edad)
values
    ('lalallele@correo.com', 'lalalchanchito', 30);

select *
from Usuario;

select *
from Usuario
where edad > 31;
/*edad mayor a 31*/

select *
from Usuario
where edad < 31;
/*edad menor a 31*/

update Usuario set edad = 32 where id = "1";
/*si no coloco where la condicion me actualiza todo los registros
a 32, con id le indico a  cual*/

delete from Usuario where id = "1"
/*si no le colocamos el where nos elimina todo en este caso
no ya que estamos en mysql worbech pero si nos conectamos a una instancia son 
worbech a mysql se elimina todo el ususario*/

