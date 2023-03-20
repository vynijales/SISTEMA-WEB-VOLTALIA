function findIndexById(list, id) {
    for (let i = 0; i < list.length; i++) {
      if (list[i][2] == id) {
        return i;
      }
    }
    // Se o id não for encontrado, retorna -1
    return -1;
  }