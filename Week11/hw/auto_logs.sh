#!/bin/bash

SOURCE_DIRS="/etc"
BACKUP_DIR="/backup"
DATE=$(date +%y-%m-%d_%H-%M-%S)
BACKUP_NAME="backup_$DATE.tar.gz"
rem_day=7

echo "Backup Start"
mkdir -p "$BACKUP_DIR"
tar -czf "$BACKUP_DIR/$BACKUP_NAME" $SOURCE_DIRS