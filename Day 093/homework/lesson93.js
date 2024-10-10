document.addEventListener('DOMContentLoaded', () => {
    const taskInput = document.getElementById('task-input');
    const addTaskButton = document.getElementById('add-task');
    const taskList = document.getElementById('task-list');
    const clearTasksButton = document.getElementById('clear-tasks');

    loadTasks();

    addTaskButton.addEventListener('click', () => {
        const taskText = taskInput.value.trim();
        if (taskText) {
            addTask(taskText);
            taskInput.value = ''; 
        }
    });

    clearTasksButton.addEventListener('click', clearAllTasks);

    function addTask(taskText) {
        const li = document.createElement('li');
        li.innerHTML = `
            <input type="checkbox" class="task-checkbox">
            <span class="task-text">${taskText}</span>
            <button class="delete-task">Delete</button>
        `;

        taskList.appendChild(li);

        li.querySelector('.task-checkbox').addEventListener('change', (e) => {
            const taskTextElement = li.querySelector('.task-text');
            if (e.target.checked) {
                taskTextElement.classList.add('completed');
            } else {
                taskTextElement.classList.remove('completed');
            }
            saveTasks(); 
        });

        li.querySelector('.delete-task').addEventListener('click', () => {
            taskList.removeChild(li);
            saveTasks(); 
        });

        saveTasks(); 
    }

    function clearAllTasks() {
        taskList.innerHTML = '';
        saveTasks(); 
    }

    function saveTasks() {
        const tasks = [];
        taskList.querySelectorAll('li').forEach(li => {
            const taskText = li.querySelector('.task-text').textContent;
            const isCompleted = li.querySelector('.task-checkbox').checked;
            tasks.push({ text: taskText, completed: isCompleted });
        });
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }

    function loadTasks() {
        const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
        tasks.forEach(task => {
            addTask(task.text);
            if (task.completed) {
                const lastTask = taskList.lastChild;
                lastTask.querySelector('.task-checkbox').checked = true;
                lastTask.querySelector('.task-text').classList.add('completed');
            }
        });
    }
});