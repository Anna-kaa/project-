/* site/config.js
 * Все балансные настройки игры «Трафик-Контроль: Спасение Центра».
 * В script.js нет ни одного числа баланса — только чтение из этого объекта.
 * Файл должен подключаться в index.html ДО script.js.
 */

const CONFIG = {
  /* ---------------- Карта ---------------- */
  map: {
    width: 900,
    height: 620,
    roadWidth: 54,
    slotSize: 46,

    // Один фиксированный маршрут: въезд с кольца -> центр города.
    // Сложный pathfinding не используется, движение идёт по точкам.
    waypoints: [
      { x: -20, y: 90 },
      { x: 250, y: 90 },
      { x: 250, y: 340 },
      { x: 560, y: 340 },
      { x: 560, y: 150 },
      { x: 920, y: 150 }
    ],

    // 8 фиксированных строительных площадок вдоль дороги
    slots: [
      { x: 110, y: 200 },
      { x: 330, y: 200 },
      { x: 330, y: 450 },
      { x: 430, y: 250 },
      { x: 640, y: 250 },
      { x: 640, y: 420 },
      { x: 800, y: 250 },
      { x: 450, y: 470 }
    ]
  },

  /* ---------------- Декор карты ---------------- */
  decor: {
    parks: [
      { x: 40, y: 380, w: 200, h: 200 },
      { x: 600, y: 470, w: 240, h: 130 }
    ],
    buildings: [
      { x: 40, y: 18, w: 120, h: 44 },
      { x: 610, y: 20, w: 90, h: 58 },
      { x: 770, y: 330, w: 110, h: 70 },
      { x: 380, y: 380, w: 78, h: 48 }
    ],
    trees: [
      { x: 90, y: 430, r: 16 },
      { x: 170, y: 500, r: 14 },
      { x: 660, y: 530, r: 16 },
      { x: 780, y: 540, r: 13 },
      { x: 300, y: 40, r: 14 },
      { x: 700, y: 90, r: 12 }
    ]
  },

  /* ---------------- Типы защиты (3 уровня) ---------------- */
  // slow — множитель скорости врага: 0.62 = замедление на 38%
  towers: {
    drone: {
      name: 'Дрон-регулировщик',
      short: 'Дрон',
      cost: 40,
      color: '#3d7dd6',
      upgradeCost: [35, 60],
      levels: [
        { damage: 8, radius: 120, cooldown: 380 },
        { damage: 12, radius: 135, cooldown: 330 },
        { damage: 17, radius: 150, cooldown: 290 }
      ]
    },
    light: {
      name: 'Умный светофор',
      short: 'Светофор',
      cost: 60,
      color: '#e6b422',
      upgradeCost: [50, 80],
      levels: [
        { damage: 3, radius: 150, cooldown: 900, slow: 0.62 },
        { damage: 4, radius: 170, cooldown: 840, slow: 0.56 },
        { damage: 6, radius: 190, cooldown: 780, slow: 0.50 }
      ]
    },
    evac: {
      name: 'Эвакуаторный пост',
      short: 'Эвакуатор',
      cost: 100,
      color: '#8a5cd1',
      upgradeCost: [70, 110],
      levels: [
        { damage: 34, radius: 190, cooldown: 1400 },
        { damage: 48, radius: 210, cooldown: 1300 },
        { damage: 65, radius: 230, cooldown: 1200 }
      ]
    }
  },

  // Порядок вывода в меню постройки (и горячие клавиши 1-2-3)
  towerOrder: ['drone', 'light', 'evac'],
  maxLevel: 3,

  /* ---------------- Экономика ---------------- */
  economy: {
    startBudget: 160,   // хватает на 2-3 базовых объекта
    capacity: 15,       // пропускная способность Центра (аналог жизней)
    killReward: 12,     // бюджет за разгруженную машину
    sellRefund: 0.5,    // 50% вложенного бюджета при демонтаже
    waveClearBonus: [45, 60, 75, 90, 120]
  },

  /* ---------------- Волны: рост сложности ---------------- */
  // count — машин в волне, hp — прочность, speed — px/сек, interval — мс между машинами
  waves: [
    { count: 7,  hp: 26, speed: 70,  interval: 950 },
    { count: 10, hp: 34, speed: 80,  interval: 880 },
    { count: 13, hp: 44, speed: 92,  interval: 800 },
    { count: 17, hp: 57, speed: 102, interval: 720 },
    { count: 21, hp: 74, speed: 112, interval: 650 }
  ],

  /* ---------------- Цвета ---------------- */
  colors: {
    ground: '#f2f7f2',
    road: '#c3cbd6',
    roadEdge: '#9aa5b1',
    roadLine: '#ffffff',
    car: '#e8645f',
    carTop: '#f6b0ab',
    hpGood: '#2e9e5b',
    hpWarn: '#e6a817',
    hpBad: '#d94b3d'
  }
};
