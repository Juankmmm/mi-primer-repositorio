CREATE TABLE matricula (
    id_matricula SERIAL PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_curso INT NOT NULL,
    fecha_matricula DATE NOT NULL,
    
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
);

SELECT * FROM estudiante;

SELECT * FROM curso;

INSERT INTO matricula (id_estudiante, id_curso, fecha_matricula)
VALUES (4, 2, '2026-08-18');

SELECT * FROM matricula;

SELECT 
    estudiante.nombre,
    estudiante.apellido,
    curso.nombre_curso,
    matricula.fecha_matricula
FROM matricula
INNER JOIN estudiante
    ON matricula.id_estudiante = estudiante.id_estudiante
INNER JOIN curso
    ON matricula.id_curso = curso.id_curso;

	SELECT id_estudiante, nombre, apellido FROM estudiante;