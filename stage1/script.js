const steps = [
  'עיבוד הפקודה',
  'בדיקת קישוריות עם המצלמה',
  'בדיקת חיבור סיריאלי לזרוע הרובוטית',
  'תחילת סריקה',
  'ניסיון זיהוי',
  'זיהוי + תצוגת Bounding Box',
  'תנועה לכיוון האובייקט',
  'שיפור זווית הגריפר',
  'נסיון תפיסה של החפץ',
  'אחיזה מוצלחת',
  'הרמה והנחה במקום קבוע',
  'הפעולה הושלמה'
];

let interfaceType = null;

function setInterface(type) {
  interfaceType = type;
  document.getElementById('object-selection').style.display = 'block';
}

function chooseObject(objName) {
  alert(`נבחר: ${objName} (${interfaceType === 'voice' ? 'בקול' : 'במגע'})`);
  startSimulation();
}

function startSimulation() {
  document.getElementById('status-section').style.display = 'block';
  const stepsContainer = document.getElementById('steps');
  stepsContainer.innerHTML = '';
  let i = 0;
  const bar = document.getElementById('bar');

  function nextStep() {
    if (i < steps.length) {
      const div = document.createElement('div');
      div.className = 'step active';
      div.textContent = `\u2705 ${steps[i]}`;
      stepsContainer.appendChild(div);
      bar.style.width = `${((i+1)/steps.length)*100}%`;
      i++;
      setTimeout(nextStep, 1000);
    }
  }

  nextStep();
}
