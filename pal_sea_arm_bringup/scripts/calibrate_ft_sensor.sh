#!/bin/bash

# Check if the slave position is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <slave_position>"
    exit 1
fi

SLAVE_POSITION=$1

# Function to check the calibration status
check_calibration_status() {
    local status
    while true; do
        # Extract the second field from the ethercat upload output
        status=$(ethercat upload -p "$SLAVE_POSITION" 0x6010 0 --type uint32 | awk '{print $2}')
        
        if [ "$status" -eq 3 ]; then
            echo "Calibration ongoing..."
            sleep 1
        else
            echo "Calibration complete."
            break
        fi
    done
}

# Main script
echo "Setting EtherCAT slave $SLAVE_POSITION to PREOP state..."
ethercat states -p "$SLAVE_POSITION" PREOP
sleep 0.2

echo "Writing to register 0xFB01, subindex 1 on slave $SLAVE_POSITION..."
ethercat download -p "$SLAVE_POSITION" 0xFB01 1 --type uint16 1
sleep 0.2

echo "Setting EtherCAT slave $SLAVE_POSITION to OP state..."
ethercat states -p "$SLAVE_POSITION" OP

echo "Waiting for calibration to complete on slave $SLAVE_POSITION..."
check_calibration_status


