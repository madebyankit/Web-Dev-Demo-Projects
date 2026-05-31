import { useState } from "react";

export default function Player({
	initialName,
	symbol,
	isActive,
	onNameChange,
}) {
	const [isEditing, setIsEditing] = useState(false);
	const [playerName, setPlayerName] = useState(initialName);

	function handleEditClick() {
		setIsEditing((editing) => !editing);
		//(editing) => !editing is the same as !isEditing
		//but it is more reliable because it uses the previous state value
		//instead of the current state value which might be stale due to closures)
	}
	function handleChange(event) {
		setPlayerName(event.target.value);
		if (isEditing) {
			onNameChange(symbol, playerName);
		}
	}

	let editablePlayerName = <span className="player-name">{playerName}</span>;
	// let btnCaption = 'Edit';

	if (isEditing) {
		editablePlayerName = (
			<input type="text" required value={playerName} onChange={handleChange} />
		);
		// btnCaption = 'Save';
	}

	return (
		<li className={isActive ? "active" : undefined}>
			<span className="player">
				{editablePlayerName}
				<span className="player-symbol">{symbol}</span>
			</span>
			<button onClick={handleEditClick}>{isEditing ? "Save" : "Edit"}</button>
		</li>
	);
}
