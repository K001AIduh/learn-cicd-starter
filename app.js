// DOM Elements
const noteTitleInput = document.getElementById('note-title');
const noteContentInput = document.getElementById('note-content');
const saveNoteButton = document.getElementById('save-note');
const notesContainer = document.getElementById('notes-container');

// Global Variables
let notes = [];
let editingNoteId = null;

// Initialize the application
function init() {
  loadNotes();
  renderNotes();
  saveNoteButton.addEventListener('click', saveNote);
}

// Load notes from localStorage
function loadNotes() {
  const storedNotes = localStorage.getItem('notes');
  if (storedNotes) {
    notes = JSON.parse(storedNotes);
  }
}

// Save notes to localStorage
function saveNotesToStorage() {
  localStorage.setItem('notes', JSON.stringify(notes));
}

// Create a new note or update an existing one
function saveNote() {
  const title = noteTitleInput.value.trim();
  const content = noteContentInput.value.trim();

  if (!title || !content) {
    alert('Please enter both title and content for your note.');
    return;
  }

  if (editingNoteId === null) {
    // Create new note
    const note = {
      id: Date.now(),
      title: title,
      content: content,
      createdAt: new Date().toLocaleString(),
    };

    notes.push(note);
  } else {
    // Update existing note
    const noteIndex = notes.findIndex((note) => note.id === editingNoteId);
    if (noteIndex !== -1) {
      notes[noteIndex].title = title;
      notes[noteIndex].content = content;
      notes[noteIndex].updatedAt = new Date().toLocaleString();
    }

    editingNoteId = null;
    saveNoteButton.textContent = 'Save Note';
  }

  saveNotesToStorage();
  renderNotes();
  clearForm();
}

// Delete a note
function deleteNote(id) {
  notes = notes.filter((note) => note.id !== id);
  saveNotesToStorage();
  renderNotes();
}

// Edit a note
function editNote(id) {
  const note = notes.find((note) => note.id === id);
  if (note) {
    noteTitleInput.value = note.title;
    noteContentInput.value = note.content;
    editingNoteId = id;
    saveNoteButton.textContent = 'Update Note';
  }
}

// Clear the form
function clearForm() {
  noteTitleInput.value = '';
  noteContentInput.value = '';
}

// Render all notes
function renderNotes() {
  notesContainer.innerHTML = '';

  if (notes.length === 0) {
    notesContainer.innerHTML =
      '<p class="no-notes">No notes yet. Create your first note!</p>';
    return;
  }

  notes.forEach((note) => {
    const noteElement = document.createElement('div');
    noteElement.className = 'note';
    noteElement.innerHTML = `
            <h3>${note.title}</h3>
            <p>${note.content}</p>
            <div class="note-meta">
                <small>Created: ${note.createdAt}</small>
                ${
                  note.updatedAt
                    ? `<small>Updated: ${note.updatedAt}</small>`
                    : ''
                }
            </div>
            <div class="note-actions">
                <button class="edit-note" data-id="${note.id}">Edit</button>
                <button class="delete-note" data-id="${note.id}">Delete</button>
            </div>
        `;

    notesContainer.appendChild(noteElement);

    // Add event listeners
    noteElement
      .querySelector('.delete-note')
      .addEventListener('click', function () {
        deleteNote(note.id);
      });

    noteElement
      .querySelector('.edit-note')
      .addEventListener('click', function () {
        editNote(note.id);
      });
  });
}

// Initialize the app when the DOM is loaded
document.addEventListener('DOMContentLoaded', init);
