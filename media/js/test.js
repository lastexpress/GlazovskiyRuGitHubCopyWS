$('.autoplay').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
});

function showBook(category, e) {
    e.preventDefault(); // Это не вызовет ошибку, если e передан корректно

    // Скрываем все категории
    document.querySelectorAll(".book-category").forEach(function(el) {
        el.style.display = "none";
    });

    // Отображаем выбранную категорию
    if (category === "all") {
        document.getElementById("all-Books").style.display = "flex";
    } else if (category === "crypto") {
        document.getElementById("crypto-Books").style.display = "flex";
    } else if (category === "prog") {
        document.getElementById("prog-Books").style.display = "flex";
    }
}


document.querySelectorAll('.items-ph').forEach(item => {
 item.addEventListener('click', function(event) {
 event.preventDefault(); // Отменяем переход по ссылке
 const newImage = this.getAttribute('data-img'); // Получаем путь к изображению

 // Лог для проверки получаемого значения
 console.log('Полученный путь к изображению:', newImage);
 if (newImage) {
  document.getElementById('mainImage').src = newImage;
 } else {
  console.error('Не удалось получить путь к изображению:', newImage);
  }
 });
});




// const suits = ['♠', '♥', '♦', '♣'];
// const values = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];
// let deck = [];
// let players = [];
// let numPlayers; // Количество игроков
// let transferLog = []; // Лог передачи карт

// // Создание колоды
// function createDeck() {
//     deck = [];
//     for (let suit of suits) {
//         for (let value of values) {
//             deck.push(value + suit);
//         }
//     }
// }

// // Перетасовка колоды
// function shuffleDeck() {
//     for (let i = deck.length - 1; i > 0; i--) {
//         const j = Math.floor(Math.random() * (i + 1));
//         [deck[i], deck[j]] = [deck[j], deck[i]];
//     }
// }

// // Раздача карт
// function dealCards() {
//     players = Array.from({ length: numPlayers }, () => ({
//         cards: [],
//         viewed: false
//     }));

//     // Раздача карт до окончания колоды
//     let currentPlayer = 0;
//     while (deck.length > 0) {
//         players[currentPlayer].cards.push(deck.pop());
//         currentPlayer = (currentPlayer + 1) % numPlayers; // Переход к следующему игроку
//     }

//     updateDisplay();
// }

// // Игрок смотрит свои карты
// function playerViewsCards(playerIndex) {
//     players[playerIndex].viewed = true;
//     alert(`Игрок ${playerIndex + 1} посмотрел свои карты!`);

//     // Передача карты от других игроков
//     players.forEach((player, index) => {
//         if (index !== playerIndex) {
//             giveCardFromPlayer(playerIndex, index);
//         }
//     });
// }

// // Функция для передачи карты от игрока
// function giveCardFromPlayer(receiverIndex, giverIndex) {
//     const giver = players[giverIndex];
//     const receiver = players[receiverIndex];

//     const cardToGive = prompt(`Игрок ${giverIndex + 1}, выберите карту, чтобы отдать Игроку ${receiverIndex + 1}: ${giver.cards.join(', ')}`);
    
//     // Проверяем, есть ли такая карта у игрока
//     if (giver.cards.includes(cardToGive)) {
//         giver.cards.splice(giver.cards.indexOf(cardToGive), 1); // Удаляем карту у отдающего
//         receiver.cards.push(cardToGive); // Передаем карту получателю

//         // Запись передачи в лог
//         transferLog.push(`Игрок ${giverIndex + 1} отдал карту ${cardToGive} Игроку ${receiverIndex + 1}.`);
//         updateTransferLog();

//         alert(`Карта ${cardToGive} передана Игроку ${receiverIndex + 1}.`);
//     } else {
//         alert('У вас нет такой карты!');
//     }

//     updateDisplay();
// }

// // Функция для обновления лога передач
// function updateTransferLog() {
//     const logDiv = document.getElementById('transferLog');
//     logDiv.innerHTML = transferLog.map(entry => `<div>${entry}</div>`).join('');
// }

// // Обновление отображения игроков
// function updateDisplay() {
//     const playersDiv = document.getElementById('players');
//     playersDiv.innerHTML = '';

//     players.forEach((player, index) => {
//         const playerDiv = document.createElement('div');
//         playerDiv.classList.add('player');
//         playerDiv.innerHTML = `Игрок ${index + 1}: ${player.cards.length} карт ${player.viewed ? '(посмотрел)' : ''}`;
//         playerDiv.addEventListener('click', () => playerViewsCards(index)); // Добавление клика по игроку
//         playersDiv.appendChild(playerDiv);
//     });
// }

// // Событие при нажатии кнопки "Начать раздачу"
// document.getElementById('start').addEventListener('click', () => {
//     numPlayers = parseInt(document.getElementById('numPlayers').value);
//     if (numPlayers < 2 || numPlayers > 5) {
//         alert('Выберите количество игроков от 2 до 5.');
//         return;
//     }

//     createDeck();
//     shuffleDeck();
//     dealCards();
// });
// -----------------------------------------------------------------------------------------------------------------






// document.addEventListener('DOMContentLoaded', function() {
//     const playerForm = document.getElementById('playerForm');
//     const cardTable = document.getElementById('cardTable');
//     const infoMessage = document.getElementById('infoMessage');

//     // Массив с иконками для игроков
//     const icons = [
//         'bi-person-circle',   // Иконка для игрока 1
//         'bi-person-fill',     // Иконка для игрока 2
//         'bi-emoji-smile',     // Иконка для игрока 3
//         'bi-emoji-laughing',  // Иконка для игрока 4
//         'bi-emoji-sunglasses',// Иконка для игрока 5
//         'bi-emoji-heart-eyes' // Иконка для игрока 6
//     ];

//     // Функция для добавления игроков
//     function addPlayers(numPlayers) {
//         // Очищаем стол перед добавлением новых игроков
//         cardTable.innerHTML = '';

//         // Список позиций для каждого игрока
//         const positions = [
//             'player-1', 'player-2', 'player-3',
//             'player-4', 'player-5', 'player-6'
//         ];

//         // Создаем нужное количество игроков
//         for (let i = 0; i < numPlayers; i++) {
//             const playerDiv = document.createElement('div');
//             playerDiv.className = `player ${positions[i]}`;
            
//             // Добавляем иконку игрока
//             playerDiv.innerHTML = `
//                 <i class="bi ${icons[i]}"></i>
//                 <span>Player ${i + 1}</span>
//                 <div id="cards-${i + 1}" class="player-cards"></div> <!-- Контейнер для карт -->
//             `;
//             cardTable.appendChild(playerDiv);
//         }
//     }

//     // Функция для раздачи одной карты игрокам
//     function dealOneCard(playerIndex, cardNumber) {
//         const playerCardsContainer = document.getElementById(`cards-${playerIndex + 1}`);
//         if (!playerCardsContainer) {
//             console.error(`Контейнер для карт игрока ${playerIndex + 1} не найден`);
//             return;
//         }

//         // Создаем элемент карты (рубашкой вверх)
//         const cardDiv = document.createElement('div');
//         cardDiv.className = 'card back';
//         cardDiv.textContent = '🂠'; // Рубашка карты (можно заменить изображением или символом)

//         // Добавляем карту в контейнер игрока
//         playerCardsContainer.appendChild(cardDiv);
//     }

//     // Основная функция для круговой раздачи карт
//     function dealCards(numPlayers) {
//         const totalCardsPerPlayer = 3;  // Каждому игроку 3 карты
//         const totalRounds = totalCardsPerPlayer;  // Количество кругов раздачи = 3
//         let dealtCards = 0;  // Счетчик всех розданных карт

//         // Функция для раздачи карты игрокам по кругу
//         function dealNextCard() {
//             const currentRound = Math.floor(dealtCards / numPlayers);  // Текущий круг раздачи
//             const currentPlayer = dealtCards % numPlayers;  // Текущий игрок

//             // Раздаём карту текущему игроку
//             if (currentRound < totalRounds) {
//                 dealOneCard(currentPlayer, currentRound);
//                 dealtCards++;
//             }

//             // Если все карты розданы, продолжаем круги
//             if (dealtCards < numPlayers * totalRounds) {
//                 setTimeout(dealNextCard, 1000);  // Задержка для имитации круговой раздачи
//             } else {
//                 // После раздачи всех карт кладём оставшуюся стопку в центр
//                 placeRemainingStack();
//                 updateInfoMessage(`Раздача завершена. Каждому игроку роздано по ${totalCardsPerPlayer} карты.`);
//             }
//         }

//         // Запуск раздачи
//         dealNextCard();
//     }

//     // Функция для размещения оставшейся стопки карт в центре стола
//     function placeRemainingStack() {
//         const stackDiv = document.createElement('div');
//         stackDiv.className = 'card-stack';
//         stackDiv.textContent = '🂠';  // Рубашка стопки (можно заменить изображением или символом)

//         // Добавляем стопку на стол
//         cardTable.appendChild(stackDiv);
//     }

//     // Функция для вывода сообщения
//     function updateInfoMessage(message) {
//         infoMessage.textContent = message;
//     }

//     // Обработчик формы
//     playerForm.addEventListener('submit', function(event) {
//         event.preventDefault();
//         const numPlayers = parseInt(document.getElementById('numPlayers').value);
//         addPlayers(numPlayers);
//         updateInfoMessage(`${numPlayers} игрока(ов) создали стол.`);

//         // Начинаем раздачу карт
//         setTimeout(() => dealCards(numPlayers), 2000);  // Задержка перед раздачей
//     });

// });

// -----------------------------------------------------------------------------------------------------------------------





// document.addEventListener('DOMContentLoaded', function() {
//     const playerForm = document.getElementById('playerForm');
//     const cardTable = document.getElementById('cardTable');
//     const infoMessage = document.getElementById('infoMessage');
//     const remainingCardsDisplay = document.getElementById('remainingCards'); // Добавляем элемент для отображения оставшихся карт

//     // Массив с иконками для игроков
//     const icons = [
//         'bi-person-circle',   // Иконка для игрока 1
//         'bi-person-fill',     // Иконка для игрока 2
//         'bi-emoji-smile',     // Иконка для игрока 3
//         'bi-emoji-laughing',  // Иконка для игрока 4
//         'bi-emoji-sunglasses',// Иконка для игрока 5
//         'bi-emoji-heart-eyes' // Иконка для игрока 6
//     ];

//     // Создание колоды из 36 карт
//     const suits = ['♠', '♥', '♦', '♣']; // Масти: пики, черви, бубны, трефы
//     const values = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']; // Значения карт
//     let deck = [];

//     // Создаем колоду
//     function createDeck() {
//         deck = [];
//         for (let suit of suits) {
//             for (let value of values) {
//                 deck.push(`${value}${suit}`);
//             }
//         }
//     }

//     // Перемешивание колоды
//     function shuffleDeck() {
//         for (let i = deck.length - 1; i > 0; i--) {
//             const j = Math.floor(Math.random() * (i + 1));
//             [deck[i], deck[j]] = [deck[j], deck[i]];
//         }
//     }

//     // Функция для добавления игроков
//     function addPlayers(numPlayers) {
//         cardTable.innerHTML = ''; // Очищаем стол

//         const positions = [
//             'player-1', 'player-2', 'player-3',
//             'player-4', 'player-5', 'player-6'
//         ];

//         for (let i = 0; i < numPlayers; i++) {
//             const playerDiv = document.createElement('div');
//             playerDiv.className = `player ${positions[i]}`;
            
//             playerDiv.innerHTML = `
//                 <i class="bi ${icons[i]}"></i>
//                 <span>Player ${i + 1}</span>
//                 <div id="cards-${i + 1}" class="player-cards"></div>
//             `;
//             cardTable.appendChild(playerDiv);
//         }
//     }

//     // Функция для раздачи одной карты игроку (лицом вниз или лицом вверх)
//     function dealOneCard(playerIndex, card, faceUp = false) {
//         const playerCardsContainer = document.getElementById(`cards-${playerIndex + 1}`);
//         if (!playerCardsContainer) {
//             console.error(`Контейнер для карт игрока ${playerIndex + 1} не найден`);
//             return;
//         }

//         const cardDiv = document.createElement('div');
//         cardDiv.className = `card ${faceUp ? 'face-up' : 'back'}`;
//         cardDiv.textContent = faceUp ? card : '🂠'; // Показываем карту либо лицом вверх, либо рубашкой

//         playerCardsContainer.appendChild(cardDiv);
//     }

//     // Функция для создания стопки карт
//     function createCardStack(playerIndex) {
//         const playerCardsContainer = document.getElementById(`cards-${playerIndex + 1}`);
//         const stackDiv = document.createElement('div');
//         stackDiv.className = 'card-stack';
//         stackDiv.textContent = '🂠';  // Символ рубашки карты для стопки

//         playerCardsContainer.innerHTML = ''; // Очищаем предыдущие карты
//         playerCardsContainer.appendChild(stackDiv); // Добавляем стопку вместо 3 карт
//     }

//     // Функция для обновления информации о количестве оставшихся карт
//     function updateRemainingCards() {
//         remainingCardsDisplay.textContent = `Осталось карт в колоде: ${deck.length}`;
//     }

//     // Основная функция для раздачи карт
//     function dealCards(numPlayers) {
//         createDeck(); // Создаем новую колоду
//         shuffleDeck(); // Тасуем колоду

//         let dealtCards = 0;

//         // Функция для раздачи по 3 карты каждому игроку лицом вниз (стопка)
//         function dealFirstThreeCards() {
//             for (let i = 0; i < 3; i++) {
//                 for (let j = 0; j < numPlayers; j++) {
//                     dealOneCard(j, deck[dealtCards], false); // Лицом вниз
//                     dealtCards++;
//                 }
//             }
//             deck.splice(0, dealtCards); // Убираем розданные карты из колоды
//             updateRemainingCards(); // Обновляем количество оставшихся карт
//         }

//         // Убираем три карты как стопку
//         function hideCardStack() {
//             for (let j = 0; j < numPlayers; j++) {
//                 createCardStack(j); // Создаем визуальную стопку карт для каждого игрока
//             }
//         }

//         // Функция для раздачи по одной карте лицом вниз и одной лицом вверх каждому игроку
//         function dealNextTwoCards() {
//             for (let j = 0; j < numPlayers; j++) {
//                 // Раздаём одну карту лицом вниз
//                 dealOneCard(j, deck[dealtCards], false);
//                 dealtCards++;

//                 // Раздаём одну карту лицом вверх
//                 dealOneCard(j, deck[dealtCards], true);
//                 dealtCards++;
//             }
//             deck.splice(0, dealtCards); // Убираем розданные карты из колоды
//             updateRemainingCards(); // Обновляем количество оставшихся карт
//         }

//         // Функция для размещения оставшейся стопки карт в центре стола
//         function placeRemainingStack() {
//             const stackDiv = document.createElement('div');
//             stackDiv.className = 'card-stack';
//             stackDiv.textContent = '🂠';  // Рубашка стопки

//             cardTable.appendChild(stackDiv);
//             updateRemainingCards(); // Обновляем количество оставшихся карт
//         }

//         // Начинаем раздачу карт
//         dealFirstThreeCards(); // Сначала раздаём по 3 карты каждому
//         setTimeout(hideCardStack, 1000); // Через секунду превращаем карты в стопку
//         setTimeout(dealNextTwoCards, 2000); // Затем раздаём по одной карте лицом вниз и одной лицом вверх
//         setTimeout(placeRemainingStack, 3000); // Кладём оставшуюся стопку карт в центр стола

//         updateInfoMessage('Раздача завершена. Карты розданы.');
//     }

//     // Функция для вывода сообщения
//     function updateInfoMessage(message) {
//         infoMessage.textContent = message;
//     }

//     // Обработчик формы
//     playerForm.addEventListener('submit', function(event) {
//         event.preventDefault();
//         const numPlayers = parseInt(document.getElementById('numPlayers').value);
//         if (numPlayers > 6 || numPlayers < 2) {
//             updateInfoMessage('Введите количество игроков от 2 до 6.');
//             return;
//         }

//         addPlayers(numPlayers);
//         updateInfoMessage(`${numPlayers} игрока(ов) создали стол.`);

//         // Начинаем раздачу карт
//         setTimeout(() => dealCards(numPlayers), 2000); // Задержка перед раздачей
//     });
// });
