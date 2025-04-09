#!/bin/bash

FT_SLAVE_TYPE="FTSensor"

# Function to get the positions of slaves of a specific type
get_slave_positions_from_type() {
    local slave_type=$1
    ethercat slaves | awk -v t="$slave_type" '$0 ~ t {print $1}'
}

# Function to check the calibration status of a specific slave
check_calibration_status() {
    local slave_position=$1
    local status
    while true; do
        # Extract the second field from the ethercat upload output
        status=$(ethercat upload -p "$slave_position" 0x6010 0 --type uint32 | awk '{print $2}')
        
        if [ "$status" -eq 3 ]; then
            echo "Calibration ongoing for slave $slave_position..."
            sleep 1
        else
            echo "Calibration complete for slave $slave_position."
            break
        fi
    done
}

# Main script
SLAVE_POSITIONS=$(get_slave_positions_from_type "$FT_SLAVE_TYPE")

if [ -z "$SLAVE_POSITIONS" ]; then
    echo "No slaves of type '$FT_SLAVE_TYPE' found."
    exit 1
fi

echo "Found slaves of type '$FT_SLAVE_TYPE' at positions: $SLAVE_POSITIONS"

# Ask the user to select which slave to calibrate
echo "Which slave do you want to calibrate?"
select SLAVE_POSITION in $SLAVE_POSITIONS; do
    if [ -n "$SLAVE_POSITION" ]; then
        echo "You selected slave $SLAVE_POSITION for calibration."
        break
    else
        echo "Invalid selection. Please try again."
    fi
done

# Perform calibration for the selected slave
echo "Setting EtherCAT slave $SLAVE_POSITION to PREOP state..."
ethercat states -p "$SLAVE_POSITION" PREOP
sleep 0.1

echo "Writing to register 0xFB01, subindex 1 on slave $SLAVE_POSITION..."
ethercat download -p "$SLAVE_POSITION" 0xFB01 1 --type uint16 1
sleep 0.1

echo "Setting EtherCAT slave $SLAVE_POSITION to OP state..."
ethercat states -p "$SLAVE_POSITION" OP

echo "Waiting for calibration to complete on slave $SLAVE_POSITION..."
check_calibration_status "$SLAVE_POSITION"

echo "Calibration process for slave $SLAVE_POSITION completed successfully."
