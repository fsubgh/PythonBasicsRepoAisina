         let tasks = [];
        function inputButton(){
            const input = document.getElementById("inputText");
            const text = input.value.trim();
            if (text === "") return;
            tasks.push(text);
            input.value = "";
            render();
        }
        function render(){
            const list = document.getElementById("Spisok");
            list.innerHTML = "";

            tasks.forEach((task, index) => {
                let li = document.createElement("li");
                li.textContent = task;

                li.onclick =() => {
                    tasks.splice(index, 1);
                    render();
                };
                list.appendChild(li);
            })
        }