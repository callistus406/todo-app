const titleElem = document.getElementById("title");
const descriptionElem = document.getElementById("description");
const priorityElem = document.getElementById("priority");
const statusElem = document.getElementById("status");
const startDateElem = document.getElementById("startDate");
const endDateElem = document.getElementById("endDate");
const todoIdElem = document.getElementById("todo_id");
const submitBtnElem = document.getElementById("submit");
const updateBtnElem = document.getElementById("update");
const deleteBtnElem = document.getElementById("delete");
console.log(submitBtnElem);
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const addTodo = () => {
  fetch("http://localhost:8000/add/todo", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: JSON.stringify({
      title: titleElem.value,
      description: descriptionElem.value,
      priority: priorityElem.value,
      status: statusElem.value,
      start_date: startDateElem.value,
      end_date: endDateElem.value,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {})
    .catch((error) => {
      console.log(error.message);
    });
};
submitBtnElem.addEventListener("click", (event) => {
  event.preventDefault();
  addTodo();
});

const updateTodo = (todo_id) => {
  fetch(`http://localhost/:8000/update/todo/${todo_id}`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify({
      title: titleElem.value,
      description: descriptionElem.value,
      priority: priorityElem.value,
      status: statusElem.value,
      start_date: startDateElem,
      end_data: endDateElem,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {})
    .catch((error) => {
      console.log(error.message);
    });
};

updateBtnElem?.addEventListener("submit", (event) => {
  event.preventDefault();
  const todo_id = todoIdElem.value;
  updateTodo(todo_id);
});

const deleteTodo = (todo_id) => {
  fetch(`http://localhost/:8000/delete/todo/${todo_id}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {})
    .catch((error) => {
      console.log(error.message);
    });
};

deleteBtnElem?.addEventListener("submit", (event) => {
  event.preventDefault();
  const todo_id = todoIdElem.value;
  deleteTodo(todo_id);
});
